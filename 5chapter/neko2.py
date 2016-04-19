#! /usr/bin/env python
# -*- coding:utf-8 -*-

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
