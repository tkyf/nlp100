#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import ngram

    sentence = 'I am an NLPer'

    word_2gram = ngram.word_ngram(sentence, 2)
    char_2gram = ngram.ngram(sentence, 2)

    print(word_2gram)
    print(char_2gram)

if __name__ == '__main__':
    main()

