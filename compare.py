#!/usr/bin/python

def isMatching(picks, winning):
  result = []
  for pick in picks:
    matching = pick[0].intersection(winning[0])
    entry = ()
    if len(matching) > 1:
      entry[0] = matching
    if (pick[1] == winning[1]):
      entry[1] = winning[1]
    result.append(entry)
  return result
