#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import ngram
    sentecne1 = 'paraparaparadise'
    sentecne2 = 'paragraph'

    X = set(ngram.ngram(sentecne1, 2))
    Y = set(ngram.ngram(sentecne2, 2))

    XYunion = X | Y
    XYintersection = X & Y
    XYdiference = X - Y
    print(X)
    print(Y)
    print(XYunion)
    print(XYintersection)
    print(XYdiference)

    if 'se' in X and 'se' in Y:
        print("'se' is in X and Y")
    else:
        print("'se' is not in X and Y")

if __name__ == '__main__':
    main()

