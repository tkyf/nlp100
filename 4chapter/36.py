#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys
from collections import defaultdict

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    text = neko.read_and_map()
    result = neko.frequency_list(text)
    print(result)

    return

if __name__ == '__main__':
    main()

