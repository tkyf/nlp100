#! /usr/bin/env python
# -*- coding:utf-8 -*-

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

            morph = {}
            morph['surface'] = surface
            morph['pos'] = pos
            morph['pos1'] = pos1
            morph['base'] = base
            sentence.append(morph)

    return text

def pick(text, key, cond=None, key2=None):
    result = []
    for sentence in text:
        for word in sentence:
            val = word[key]
            if cond:
                if val == cond:
                    if key2:
                        result.append(word[key2])
                    else:
                        result.append(word)
            else:
                result.append(val)
    return result

