#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} N".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    n = int(sys.argv[1])

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[-n:]

    for L in lines:
        print(L, end="")



if __name__ == '__main__':
    main()

# 動作確認
# $ tail -3 hightemp.txt
