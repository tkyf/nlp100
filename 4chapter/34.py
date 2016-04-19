#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    text = neko.read_and_map()
    result = neko.a_no_b(text)
    print(list(result))

    return

if __name__ == '__main__':
    main()
