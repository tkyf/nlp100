#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} N".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    N = int(sys.argv[1])

    with open("hightemp.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    rows = len(lines)
    if rows < N :
        N = rows

    quota = list(reversed([(rows + i) // N for i in range(N)]))

    current = 0
    for i in range(N):
        with open("split_{}.txt".format(i), "w", encoding="utf-8") as f:
            for line in lines[current:quota[i] + current]:
                f.write(line)
            current = current + quota[i]


if __name__ == '__main__':
    main()

# 動作確認
# $ split hightemp.txt -l $(expr $(wc -l hightemp.txt | cut -f 1 -d" ") / 5)
