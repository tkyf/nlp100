#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    lines = []

    with open("col1.txt", "r", encoding="utf-8") as col1, \
         open("col2.txt", "r", encoding="utf-8") as col2, \
         open("13.txt", "w", encoding="utf-8") as f:
        for line in zip(col1, col2):
            f.write("\t".join(map(str.strip, line)) + "\n")

if __name__ == '__main__':
    main()

# 動作確認
# $ paste col1.txt col2.txt -d "\t" > a.txt
