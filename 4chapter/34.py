#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def a_no_b(text):
    for sentence in text:
        if len(sentence) > 2 :
            for word1, word2, word3 in zip(sentence, sentence[1:], sentence[2:]):
                if word1['pos'] == '名詞' and \
                    word2['surface'] == 'の' and word3['pos'] == '名詞':
                    yield  (word1, word2, word3)

def main():
    text = neko.read_and_map()
    result = a_no_b(text)
    print(list(result))

    return

if __name__ == '__main__':
    main()

