#!/usr/bin/python

import sys

data = sys.stdin.readlines()

winning = data.pop().split()
pb = winning.pop()
winning = (set(winning), pb)

for line in data:
	line = line.split()
	pb = line.pop()
	matching = set(line).intersection(winning[0])
	if (pb == winning[1]) or (len(matching) > 1) :
		print str(line) + " " + pb + " matched with: " + str(matching) + " " + pb
	else:
		print str(line) + " " + pb + " didn't match."
