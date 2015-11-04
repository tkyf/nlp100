#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import sys
    import io
    import json
    import re

    # cp932では出力できない文字が含まれているため、出力エンコーディングをUTF-8に変更
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    with open("england.json", "r", encoding="utf-8") as f:
        j = json.load(f)

    text = j["text"]

    p = re.compile('=(=+)(.+)=')
    for L in text.split("\n"):
        m = p.search(L)
        if m:
            depth = len(m.group(1)) 
            print(depth , end=" ")
            # 閉じタグの=を取り除いて表示する
            print(m.group(2)[:-depth])

if __name__ == '__main__':
    main()

