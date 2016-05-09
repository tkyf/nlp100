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

    # 基礎情報を取り出す
    p_info = re.compile('{{基礎情報\s+国(.*?)\n}}\n', re.DOTALL)
    m = p_info.search(text)
    # 基礎情報をstrにする
    info = m.group(1)

    # 全てのフィールドの行頭が|で始まっていることを利用する。
    p_field = re.compile(r'\n\|(.+?)\s+=\s+(((?!\n\|).)*)', re.DOTALL)
    m2 = p_field.findall(info)

    p_de_emphasize = re.compile(r'\'{2,5}')
    p_remove_link = re.compile(r'\[\[(.*?)\]\]')

    # MediaWikiマークアップの除去
    p_ref = re.compile(r'<ref.*?>(.*?)</ref>')
    p_ref_single = re.compile(r'<ref.*?/>')
    p_nl = re.compile(r'<br\s*?/>')

    d = {}
    for p in m2:
        s = p_de_emphasize.sub('', p[1])
        s = p_remove_link.sub(r'\1', s)
        s = p_ref.sub(r'\1', s)
        s = p_ref_single.sub('', s)
        s = p_nl.sub('', s)
        d[p[0]] = s

    for k, v in sorted(d.items()):
        print(k, v)


if __name__ == '__main__':
    main()
