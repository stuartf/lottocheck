#!/usr/bin/python2.5

class compare():
  matches = None
  def __init__(self, picks, winning):
    self.matches = []
    for pick in picks:
      lottoNums = lottoPick()
      for num in pick[0]:
        lottoNums.numbers.append((num, (num in winning[0])))
      lottoNums.pb = (pick[1], (pick[1] == winning[1]))
      self.matches.append(lottoNums)

class lottoPick():
  numbers = None
  pb = None
  def __str__(self):
    return str(self.numbers) + " " + str(self.pb)
  def __repr__(self):
    return self.__str__()
  def __init__(self):
    self.numbers = []
