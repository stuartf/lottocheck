#!/usr/bin/python

def getMatching(picks, winning):
  result = []
  for pick in picks:
    matching = pick[0].intersection(winning[0])
    entry = []
    entry.append(matching)
    if (pick[1] == winning[1]):
      entry.append(winning[1])
    result.append(entry)
  return result
