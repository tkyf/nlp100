#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks, extract_case_frames

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    sentences = read_and_make_chunks()
    for sentence in sentences:
        case_patterns = extract_case_frames(sentence)
        if case_patterns:
            print('\n'.join(case_patterns))

if __name__ == '__main__':
    main()
