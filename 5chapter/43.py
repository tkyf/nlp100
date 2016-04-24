#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks, Chunk

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def make_phrase_exclude_symbols(chunk: Chunk):
    phrase = ""
    for morph in chunk.morphs:
        if morph.pos != '記号':
            phrase += morph.surface
    return phrase


def main():
    sentences = read_and_make_chunks()
    for chunks in sentences:
        for chunk in chunks:
            dst = chunk.dst
            if dst != -1 and '名詞' in chunk and '動詞' in chunks[dst]:
                src_phrase = make_phrase_exclude_symbols(chunk)
                dst_phrase = make_phrase_exclude_symbols(chunks[dst])
                print("{}\t{}".format(src_phrase, dst_phrase))


if __name__ == '__main__':
    main()
