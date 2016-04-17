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
    frequencies = [freq for word, freq in frequency_list]
    x = [i for i in range(len(frequencies))]

    plt.plot(x, frequencies)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

    return

if __name__ == '__main__':
    main()
