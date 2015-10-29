#! /usr/bin/env python
# -*- coding:utf-8 -*-

def ngram(sequence, n):
    if len(sequence) <= n:
        return sequence

    ngram = []

    for i in range(len(sequence) - n + 1):
        ngram.append(sequence[i:i+n])

    return ngram


def word_ngram(sequence, n):
    if type(sequence) ==  str:
        sequence = sequence.split(' ')

    return ngram(sequence, n)

