#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    import neko

    text = neko.read_and_map()
    result = neko.pick(text, 'pos', '動詞', 'base')

    print(result )
    return

if __name__ == '__main__':
    main()

