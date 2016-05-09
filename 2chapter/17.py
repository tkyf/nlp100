#! /usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    kind_of_strings = set()

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        for L in f:
            col1 = L.split("\t")[0]
            kind_of_strings.add(col1)

    print(kind_of_strings)


if __name__ == '__main__':
    main()

# 動作確認
# $ cut -f1 hightemp.txt | sort | uniq
