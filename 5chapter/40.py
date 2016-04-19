#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import neko2

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    morphs = neko2.read_and_make_morphs()
    print(morphs[2])

    return

if __name__ == '__main__':
    main()
