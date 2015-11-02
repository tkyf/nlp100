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

    result_files = []
    for i in range(N):
        result_files.append(open("split_{}.txt".format(i), "w",
            encoding="utf-8"))

    i = 0
    for line in lines:
        result_files[i].write(line)
        i = i + 1
        i = i % N

    for f in result_files:
        f.close()



if __name__ == '__main__':
    main()

