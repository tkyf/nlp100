#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    from collections import defaultdict

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        col1s = [L.split("\t")[0] for L in f]

    freq = defaultdict(int)

    for col1 in col1s:
        freq[col1] += 1

    for k, v in sorted(freq.items(), key=lambda x:x[1], reverse=True):
        print(k, v)

if __name__ == '__main__':
    main()

# 動作確認
# $ cut -f1 hightemp.txt | sort | uniq -c | sort -rk1
