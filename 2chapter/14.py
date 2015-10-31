#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} N".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    n = int(sys.argv[1])

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        for L in zip(f, range(n)):
            print(L[0], end="")

if __name__ == '__main__':
    main()

# 動作確認
# $ head hightemp.txt -n 2
