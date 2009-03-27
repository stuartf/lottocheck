#!/usr/bin/python

from urllib import urlopen
import re

def getWinning():
  date_search = """<td align="right" height='25'><span class='textblack'>"""
  num_search = """<td align="left" height='25'><span class='textblack'><b>"""
  url = urlopen('http://megamillions.com/numbers/pastdrawings.asp')
  for line in url:
    stripped = line.lstrip()
    if stripped.startswith(date_search):
      date = re.findall('\d+/\d+/\d+', line)
    elif stripped.startswith(num_search):
      groups = re.findall('(\d+,\s\d+,\s\d+,\s\d+,\s\d+).*?(\d+)', line)
      number_set = groups[0][0].split(',')
      pb = groups[0][1]
      break
  return (date, set(number_set), pb)

if __name__ == "__main__":
  winning = getWinning()
  print winning
