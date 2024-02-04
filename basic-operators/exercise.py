#!/usr/bin/python3

x = object()
y = object()

xList = [x] * 10
yList = [y] * 10
bigList = xList + yList

print('xList contains %d objects' % len(xList))
print('yList contains %d objects' % len(yList))
print('bigList contains %d objects' % len(bigList))
