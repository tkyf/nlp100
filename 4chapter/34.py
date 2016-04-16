#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    text = neko.read_and_map()
    result = []
    for sentence in text:
        while len(sentence) > 2 :
            word1, word2, word3 = sentence[:3]
            if word1['pos'] == '名詞' and \
                    word2['surface'] == 'の' and word3['pos'] == '名詞':
                result.append((word1, word2, word3))
            sentence.pop(0)
    print(result)

    return

if __name__ == '__main__':
    main()

