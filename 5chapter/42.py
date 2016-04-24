#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys
from typing import List

from neko2 import read_and_make_chunks, Morph

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def make_phrase_pair_exclude_symbols(morphs: List[Morph]):
    phrase = ""
    for morph in morphs:
        if morph.pos != '記号':
            phrase += morph.surface
    return phrase


def main():
    sentences = read_and_make_chunks()
    for chunks in sentences:
        for chunk in chunks:
            src_phrase = make_phrase_pair_exclude_symbols(chunk.morphs)
            if chunk.dst != -1:
                dst_phrase = make_phrase_pair_exclude_symbols(chunks[chunk.dst].morphs)
            else:
                dst_phrase = ''
            print('{}\t{}'.format(src_phrase, dst_phrase))


if __name__ == '__main__':
    main()
