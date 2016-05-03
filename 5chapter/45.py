#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    sentences = read_and_make_chunks()


if __name__ == '__main__':
    main()
