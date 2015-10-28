#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    import os

    word = 'パタトクカシーー'
    result = word[1::2]
    
    if os.name == 'nt':
        result = result.encode('utf-8').decode('cp932')
    
    print(result)

if __name__ == '__main__':
    main()

