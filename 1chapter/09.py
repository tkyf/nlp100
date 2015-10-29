#! /usr/bin/env python
# -*- coding:utf-8 -*-

def typoglycemia(word):
    import random

    if len(word) < 5:
        return word
    print(word)
    print(word[1:len(word) - 1])

    shuffled_sequence = ''.join(random.sample(word[1:len(word) - 1], len(word) - 2))

    return word[0] + shuffled_sequence + word[-1]




def main():
    print(typoglycemia("word"))

    sentecne = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuffled_sentence = []

    for word in sentecne.split(' '):
        shuffled_sentence.append(typoglycemia(word))
    print(' '.join(shuffled_sentence))

if __name__ == '__main__':
    main()

