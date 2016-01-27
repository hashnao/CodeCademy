#!/usr/bin/env python

answer = raw_input("Enter a word: ")
if answer != '':
    print(answer[1:] + answer[0].lower() + 'ay')
