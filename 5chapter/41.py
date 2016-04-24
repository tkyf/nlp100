#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    chunks = read_and_make_chunks()
    for chunk in chunks:
        print(chunk)
    return


if __name__ == '__main__':
    main()
