#!/usr/bin/python2.5

import sys
import winningNums
import compare

filename = "./picks"
file = open(filename)
data = file.readlines()

winning = winningNums.getWinning()
date = winning[0][0]
winning = (map(int, winning[1]), int(winning[2]))

picks = []
for line in data:
  line = line.split()
  pb = line.pop()
  picks.append((map(int, line), int(pb)))

matches = compare.getMatching(picks, winning)

header = """Content-type: text/html

<html><head><style>span{border: thin solid; padding: 2px; margin: 2px;}
div{margin:15px} .numwin{background-color:red;} .pb{background-color:yellow;}
.pbwin{background-color:blue;}</style>
<title>CETL Lotto Checker</title></head><body>"""

print header
print "<h2>Last Drawing on " + date + "</h2>",
print "<h3>Winning Numbers: ",
for number in winning[0]:
  print '<span class="num">%02d</span>' % number,
print '<span class="pb">%02d</span></h3>' % winning[1]
print matches
print "</body></html>"
