#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys
from typing import List

from neko2 import read_and_make_chunks, Chunk

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def make_phrase_exclude_symbols(chunk: Chunk):
    phrase = ''
    for morph in chunk.morphs:
        if morph.pos != '記号':
            phrase += morph.surface
    return phrase


def make_dot(chunks: List[Chunk]):
    """Chunkのリストから係り受け木を作成して返す。
    係り受け木はDOT言語の有向グラフで表現する。
    :param chunks: List[Chunk]
    :rtype: str
    """
    nodes = []
    edges = []
    for i, chunk in enumerate(chunks):
        if not chunk.is_blank():
            nodes.append(str(i) + ' [label="' + chunk.surface() + '"];\n')
            if chunk.is_depending():
                edges.append(str(i) + '->' + str(chunk.dst) + ';\n')
    head = 'digraph G ' + ' {\nnode[fontname="meiryo"];\nedge[fontname="meiryo"];\n'
    body = ''.join(nodes) + ''.join(edges)
    tail = '}'
    return head + body + tail


def main():
    sentences = read_and_make_chunks()
    dots = []
    for chunks in sentences:
        dots.append(make_dot(chunks))

    for dot in dots:
        print(dot)


if __name__ == '__main__':
    main()
