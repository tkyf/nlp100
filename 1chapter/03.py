#! /usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    words = sentence.split(' ')
    list_of_number_of_characteres = [len(word) for word in words]
    print(list_of_number_of_characteres)


if __name__ == '__main__':
    main()
