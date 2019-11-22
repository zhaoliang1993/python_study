#!/usr/bin/python

import sys
import os

name = sys.argv[0]

patch = ''
print(name)
if sys.argv[1]:
        patch = sys.argv[1]

print(patch)

dir1 = './temp'

de = os.path.exists('temp')
if not de:
        os.makedirs(dir1)


f1 = open(patch,'r')
f2 = open(r'./temp/123.txt','w+')


while True:
        w = f1.readline()
        if not w:
                break
                pass
        if '@@' in w:
                while True:
                        f2.write(w)
                        w = f1.readline()
                        if not w or '--' in w:
                                break
                                pass
f1.close()
f2.close()

f1 = open(r'./temp/123.txt','r')
f2 = open(r'./temp/out.txt','w+')

part = 0
while True:
        w = f1.readline()
        if not w:
                break
        if w[0] == '+':
                continue
        if '@@' in w:
                part = part + 1
                w = 'part'+str(part)+'\n'
                f2.write(w)
        if w[0] == ' ' or w[0] == '-':
                w = w[1:]
                f2.write(w)
