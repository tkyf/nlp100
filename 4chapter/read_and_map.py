#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

FILE = 'neko.txt.mecab'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    text = []
    with open(FILE, 'r', encoding='utf-8') as f:
        sentence = []
        for law_line in f:
            line = law_line.strip()
            if(line == 'EOS'):
                if(sentence):
                    text.append(sentence)
                    sentence = []
                continue

            if('\t' not in line):
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

    print(text)
    return

if __name__ == '__main__':
    main()

