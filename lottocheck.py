#!/usr/bin/python

import sys
import winningNums
import compare

filename = "./picks"
file = open(filename)
data = file.readlines()

winning = winningNums.getWinning()
date = winning[0]
winning = (set(winning[1]), winning[2])

picks = []
for line in data:
  line = line.split()
  pb = line.pop()
  picks.append((set(line), pb))

matches = compare.getMatching(picks, winning)

print matches
