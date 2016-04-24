#! /usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

FILE = 'neko.txt.cabocha'


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '{}({}, {}, {})'.format(self.surface, self.base, self.pos, self.pos1)

    def __repr__(self):
        return self.__str__()


class Chunk:
    def __init__(self, morphs: list = None, dst: int = None, srcs: List[int] = None):
        """
        :type srcs: List[int]
        :rtype:Chunk
        :param morphs:
        :param dst:
        :param srcs:
        """
        if morphs:
            assert isinstance(srcs, List[Morph])
            self.morphs = morphs
        else:
            self.morphs = []
        self.dst = dst

        if srcs:
            assert isinstance(srcs, List[int])
            self.srcs = srcs
        else:
            self.srcs = []

    def __str__(self):
        return '\n{}({}, {})'.format(self.morphs, self.dst, self.srcs)

    def __repr__(self):
        return self.__str__()

    def __contains__(self, pos: str):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False


def read_and_make_morphs():
    text = []
    with open(FILE, 'r', encoding='utf-8') as f:
        sentence = []
        for law_line in f:
            line = law_line.strip()
            if line[0] == '*':
                continue
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

            morph = Morph(surface, base, pos, pos1)
            sentence.append(morph)

    return text


def read_and_make_chunks():
    sentences = __read_and_make_sentences(FILE)
    for sentence in sentences:
        yield __make_chunks_from_sentence(sentence)


def __read_and_make_sentences(file):
    with open(file, 'r', encoding='utf-8') as f:
        sentence = []
        for law_line in f:
            line = law_line.strip()
            if line != 'EOS':
                sentence.append(line)
            else:
                if sentence:
                    yield sentence
                    sentence = []


def __make_chunks_from_sentence(sentence):
    def is_chunk_head(phrase):
        return phrase.startswith('* ')

    def get_dst(chunk_head):
        return int(chunk_head.split(' ')[2][:-1])

    chunks = []
    chunk = Chunk()
    for line in sentence:
        if is_chunk_head(line):
            if chunk.morphs:
                chunks.append(chunk)
            chunk = Chunk()
            chunk.dst = get_dst(line)
        else:
            chunk.morphs.append(__make_morph(line))
    if chunk.morphs:
        chunks.append(chunk)
    __set_srcs(chunks)
    return chunks


def __set_srcs(chunks):
    for i, chunk in enumerate(chunks):
        dst = chunk.dst
        if dst != -1:
            chunks[dst].srcs.append(i)


def __make_morph(line):
    if '\t' not in line:
        surface = ''
        feature = line
    else:
        surface, feature = line.split('\t')

    features = feature.split(',')
    pos = features[0]
    pos1 = features[1]
    base = features[6]

    morph = Morph(surface, base, pos, pos1)
    return morph
