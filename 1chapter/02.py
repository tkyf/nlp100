#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    string1='パトカー'
    string2='タクシー'

    result=[]
    for c1, c2 in zip(string1, string2):
        result.append(c1)
        result.append(c2)

    print(''.join(result))


if __name__ == '__main__':
    main()

