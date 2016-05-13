#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

from neko2 import read_and_make_chunks, extract_case_patterns

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    sentences = read_and_make_chunks()
    for sentence in sentences:
        case_patterns = extract_case_patterns(sentence)
        if case_patterns:
            print('\n'.join(case_patterns))

# ・コーパス中に頻出する述語と各パターンの組み合わせ
# $ python 45.py > 45.txt
# $ sort 45.txt | uniq -c | sort -r | head
# ・「する」「見る」「与える」という動詞の各パターン
# $ grep -E '^する[[:space:]]|^見る[[:space:]]|^与える[[:space:]]' 45.txt | sort | uniq -c | sort -r
if __name__ == '__main__':
    main()
