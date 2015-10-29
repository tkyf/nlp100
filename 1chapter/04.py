#! /usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    result_dict = {}
    one_character_positions = (1, 5, 6, 7, 8, 9, 15, 16, 19)

    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    for i, word in enumerate(sentence.split(' ')):
        position = i + 1

        if(position in one_character_positions):
            key_character = word[0]
        else:
            key_character = word[0:2]
        result_dict[key_character] = position

    for k, v in result_dict.items():
        print(k, v)

if __name__ == '__main__':
    main()

