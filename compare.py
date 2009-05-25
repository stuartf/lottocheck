#!/usr/bin/python2.5

def getMatching(picks, winning):
  result = ""
  for pick in picks:
    entry = "<div>"
    for num in pick[0]:
      entry += "<span class="
      if num in winning[0]:
        entry += '"numwin"'
      else:
        entry += '"num"'
      entry += ">%02d</span>" % num
    entry += '<span class='
    if (pick[1] == winning[1]):
      entry += '"pbwin"'
    else:
      entry += '"pb"'
    entry += '>%02d</span></div>' % pick[1]
    result += entry
  return result
