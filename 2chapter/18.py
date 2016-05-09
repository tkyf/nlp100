#! /usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    with open("hightemp.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    sorted_lines = sorted(lines, key=lambda line: float(line.split("\t")[2]),
                          reverse=True)

    for line in sorted_lines:
        print(line, end="")


if __name__ == '__main__':
    main()

# 動作確認
# $ sort -nrk3 hightemp.txt
