#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks, make_dot

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    sentences = read_and_make_chunks()
    dots = []
    for chunks in sentences:
        dots.append(make_dot(chunks))

    for dot in dots:
        print(dot)


if __name__ == '__main__':
    main()
