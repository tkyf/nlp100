#! /usr/bin/env python
# -*- coding:utf-8 -*-

from collections import defaultdict

FILE = 'neko.txt.mecab'


def read_and_map():
    text = []

    with open(FILE, 'r', encoding='utf-8') as f:
        sentence = []
        for law_line in f:
            line = law_line.strip()
            if line == 'EOS':
                if sentence:
                    text.append(sentence)
                    sentence = []
                continue

            if '\t' not in line:
                surface = ''
                feature = line
            else:
                surface, feature = line.split('\t')

            features = feature.split(',')
            pos = features[0]
            pos1 = features[1]
            base = features[6]

            morph = dict()
            morph['surface'] = surface
            morph['pos'] = pos
            morph['pos1'] = pos1
            morph['base'] = base
            sentence.append(morph)

    return text


def pick(text, key, cond=None, key2=None):
    for sentence in text:
        for word in sentence:
            val = word[key]
            if cond:
                if val == cond:
                    if key2:
                        yield word[key2]
                    else:
                        yield word
            else:
                yield val


def a_no_b(text):
    for sentence in text:
        if len(sentence) > 2:
            for word1, word2, word3 in zip(sentence, sentence[1:], sentence[2:]):
                if word1['pos'] == '名詞' and \
                                word2['surface'] == 'の' and word3['pos'] == '名詞':
                    yield (word1, word2, word3)


def noun_junction(text):
    for sentence in text:
        noun_junction = []
        for word in sentence:
            if word['pos'] == '名詞':
                noun_junction.append(word['surface'])
            else:
                if len(noun_junction) > 1:
                    yield "".join(noun_junction)
                noun_junction = []
        if len(noun_junction) > 1:
            yield "".join(noun_junction)


def frequency_list(text):
    result = defaultdict(int)
    for sentence in text:
        for word in sentence:
            result[(word['base'], word['pos'])] += 1

    return sorted(result.items(), key=lambda x: x[1], reverse=True)
