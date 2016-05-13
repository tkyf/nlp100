#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks, extract_LVCs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    sentences = read_and_make_chunks()
    for sentence in sentences:
        lvcs = extract_LVCs(sentence)
        if lvcs:
            print('\n'.join(lvcs))

# ・コーパス中に頻出する述語
# $ python 47.py > 47.txt
# $ cut -f1 47.txt | sort | uniq -c | sort -r | head
# ・コーパス中で頻出する述語と助詞パターン
# $ cut -f1,2 47.txt | sort | uniq -c | sort -r | head
if __name__ == '__main__':
    main()
