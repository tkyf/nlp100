#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import json
    import sys
    import io

    # cp932では出力できない文字が含まれているため、出力エンコーディングをUTF-8に変更
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    country_jsons = []
    with open("jawiki-country.json", "r", encoding="utf-8") as f:
        for L in f:
            country_jsons.append(json.loads(L))

    for j in country_jsons:
        if j["title"] == "イギリス":
            print(j["text"])

            # 以降の課題で使用するためファイルに出力しておく
            with open("england.json", "w", encoding="utf-8") as f:
                json.dump(j, f)

if __name__ == '__main__':
    main()

