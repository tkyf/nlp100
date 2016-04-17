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
    result = neko.frequency_list(text)
    top10 = result[:10]
    top10_freqs = [x[1] for x in top10]
    top10_surfaces = [x[0][0] for x in top10]
    print(top10_freqs)

    x = range(10)
    y = top10_freqs
    plt.bar(x, y, align="center")
    plt.xticks(x, top10_surfaces, fontproperties=fp)
    plt.show()

    return

if __name__ == '__main__':
    main()
