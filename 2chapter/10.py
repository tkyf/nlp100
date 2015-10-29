#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    print(len(open('hightemp.txt', 'r', encoding='utf-8').readlines()))

if __name__ == '__main__':
    main()

# 実行結果
# $ ./10.py
# 24
# $ wc -l hightemp.txt
# 24 hightemp.txt

