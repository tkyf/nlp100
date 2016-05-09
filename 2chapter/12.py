#! /usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    lines = []

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        for L in f.readlines():
            lines.append(L.split("\t"))

    with open("col1.txt", "w", encoding="utf-8") as col1, \
            open("col2.txt", "w", encoding="utf-8") as col2:
        for line in lines:
            col1.write(line[0] + "\n")
            col2.write(line[1] + "\n")


if __name__ == '__main__':
    main()

# 動作確認
# $ cut hightemp.txt -f 1
# $ cut hightemp.txt -f 2
