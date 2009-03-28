#!/usr/bin/python2.5

import sys
import winningNums
import compare

filename = "./picks"
file = open(filename)
data = file.readlines()

winning = winningNums.getWinning()
date = winning[0][0]
winning = (winning[1], winning[2])

picks = []
for line in data:
  line = line.split()
  pb = line.pop()
  picks.append((line, pb))

matches = compare.getMatching(picks, winning)

print "Content-type: text/html"
print ""
print "<html><head><style>span{border: thin solid; padding: 2px; margin: 2px;} div{margin:15px} .numwin{background-color:red;}",
print " .pb{background-color:yellow;} .pbwin{background-color:blue;}</style>",
print "<title>CETL Lotto Checker</title></head><body>",
print "<h2>Last Drawing on " + date + "</h2>",
print matches
print "</body></html>"
