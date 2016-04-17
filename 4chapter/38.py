#! /usr/bin/env python
# -*- coding:utf-8 -*-

import io
import sys

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import neko

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fp = FontProperties(fname=r"C:\WINDOWS\Fonts\meiryo.ttc", size=14)


def main():
    text = neko.read_and_map()
    frequency_list = neko.frequency_list(text)
    hist = sorted(neko.histogram(frequency_list).items())
    # 全部出すと見えないので上位10件
    hist = hist[:10]

    x = [x for x, y in hist]
    y = [y for x, y in hist]
    plt.bar(x, y)
    plt.show()

    return

if __name__ == '__main__':
    main()
