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
        noun_junction = []
        for word in sentence:
            if word['pos'] == '名詞':
                noun_junction.append(word['surface'])
            else:
                if len(noun_junction) > 1:
                    result.append("".join(noun_junction))
                noun_junction = []
        if len(noun_junction) > 1 :
            result.append("".join(noun_junction))
    print(result)

    return

if __name__ == '__main__':
    main()

