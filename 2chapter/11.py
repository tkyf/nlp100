#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    text = open('hightemp.txt', 'r', encoding='utf-8').read()
    print(text.replace('\t', ' '))

if __name__ == '__main__':
    main()


# 動作確認
# $ cat hightemp.txt | tr "\t" " "
# $ cat hightemp.txt | sed -e 's/\t/ /g'
# $ expand hightemp.txt -t 1

