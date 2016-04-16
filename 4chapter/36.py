#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys
from collections import defaultdict

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    text = neko.read_and_map()
    result = defaultdict(int)
    for sentence in text:
        for word in sentence:
            result[(word['base'], word['pos'])] += 1

    result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    print(result)

    return

if __name__ == '__main__':
    main()

