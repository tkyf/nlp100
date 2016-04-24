#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import neko2

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FILE = neko2.FILE


def read_and_make_sentences():
    text = []
    with open(FILE, 'r', encoding='utf-8') as f:
        sentence = []
        for law_line in f:
            line = law_line.strip()
            if line != 'EOS':
                sentence.append(line)
            else:
                if sentence:
                    text.append(sentence)
                    sentence = []
    return text


def make_chunks_from_sentence(sentence):
    def is_chunk_head(phrase):
        return phrase.startswith('* ')

    def get_dst(chunk_head):
        return int(chunk_head.split(' ')[2][:-1])

    chunks = []
    chunk = neko2.Chunk()
    for line in sentence:
        if is_chunk_head(line):
            if chunk.morphs:
                chunks.append(chunk)
            chunk = neko2.Chunk()
            chunk.dst = get_dst(line)
        else:
            chunk.morphs.append(make_morph(line))
    if chunk.morphs:
        chunks.append(chunk)
    set_srcs(chunks)
    return chunks


def set_srcs(chunks):
    for i, chunk in enumerate(chunks):
        dst = chunk.dst
        if dst != -1:
            chunks[dst].srcs.append(i)


def make_morph(line):
    if '\t' not in line:
        surface = ''
        feature = line
    else:
        surface, feature = line.split('\t')

    features = feature.split(',')
    pos = features[0]
    pos1 = features[1]
    base = features[6]

    morph = neko2.Morph(surface, base, pos, pos1)
    return morph


def main():
    sentences = read_and_make_sentences()
    print(sentences)
    sentences_of_chunks = []
    for sentence in sentences:
        sentences_of_chunks.append(make_chunks_from_sentence(sentence))
    print(sentences_of_chunks)
    return


if __name__ == '__main__':
    main()
