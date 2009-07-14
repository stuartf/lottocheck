#!/usr/bin/python2.5

import sys
import winningNums
import compare

filename = "./picks"
file = open(filename)
data = file.readlines()

winning = winningNums.getWinning(2)
date1 = winning[0][0][0]
winning1 = (map(int, winning[0][1]), int(winning[0][2]))
date2 = winning[1][0][0]
winning2 = (map(int, winning[1][1]), int(winning[1][2]))

picks = []
for line in data:
  line = line.split()
  pb = line.pop()
  picks.append((map(int, line), int(pb)))

matches1 = compare.getMatching(picks, winning1)
matches2 = compare.getMatching(picks, winning2)

header = """Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">

<head><style type="text/css">span{border: thin solid; padding: 2px; margin: 2px;}
div{margin:15px} .numwin{background-color:red;} .pb{background-color:yellow;}
.pbwin{background-color:blue;}</style>
<title>CETL Lotto Checker</title></head><body>"""

print header
print "<h2>Last Drawing on " + date1 + "</h2>",
print "<h3>Winning Numbers: ",
for number in winning1[0]:
  print '<span class="num">%02d</span>' % number,
print '<span class="pb">%02d</span></h3>' % winning1[1]
print matches1
print "<h2>Previous Drawing on " + date2 + "</h2>",
print "<h3>Winning Numbers: ",
for number in winning2[0]:
  print '<span class="num">%02d</span>' % number,
print '<span class="pb">%02d</span></h3>' % winning2[1]
print matches2
print "</body></html>"
