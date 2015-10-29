#! /usr/bin/env python
# -*- coding:utf-8 -*-

def cipher(text):
    ciphertext = []

    for c in text:
        if 97 <= ord(c) <= 122:
            ciphertext.append(chr(219 - ord(c)))
        else:
            ciphertext.append(c)

    return ''.join(ciphertext)

def main():
    message = "テストtestTEST!!??"
    encrypted_message = cipher(message)
    print(encrypted_message)
    print(cipher(encrypted_message))


if __name__ == '__main__':
    main()

