#!/usr/bin/python2.7

import sys
import winningNums
from compare import compare

from jinja2 import Template

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

matches1 = compare(picks, winning1)
matches2 = compare(picks, winning2)

#TODO simplify the repetative parts of this and put it in a separate template file
template = Template("""Content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
  <meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
  <style type="text/css">
    span{border: thin solid; padding: 2px; margin: 2px;}
    div{margin:15px}
    .numwin{background-color:red;}
    .pb{background-color:yellow;}
    .pbwin{background-color:blue;}
  </style>
  <title>CETL Lotto Checker</title>
</head>
<body>
  <h2>Last Drawing on {{ date1 }}</h2>
<h3>Winning Numbers: 
{% for number in winning1[0] %}
  <span class="num">{{ "%02d" |format(number) }}</span>
{% endfor %}
<span class="pb">{{ "%02d" |format(winning1[1]) }}</span></h3>
{% for match in matches1.matches %}
  <div>
  {% for num in match.numbers %}
    {% if num[1] %}
      <span class="numwin">{{ "%02d" |format(num[0]) }}</span>
    {% else %}
      <span class="num">{{ "%02d" |format(num[0]) }}</span>
    {% endif %}
  {% endfor %}
  {% if match.pb[1] %}
    <span class="pbwin">{{ "%02d" |format(match.pb[0]) }}</span>
  {% else %}
    <span class="pb">{{ "%02d" |format(match.pb[0]) }}</span>
  {% endif %}
  </div>
{% endfor %}
<h2>Previous Drawing on {{ date2 }}</h2>
<h3>Winning Numbers: 
{% for number in winning2[0] %}
  <span class="num">{{ "%02d" |format(number) }}</span>
{% endfor %}
<span class="pb">{{ "%02d" |format(winning2[1]) }}</span></h3>
{% for match in matches2.matches %}
  <div>
  {% for num in match.numbers %}
    {% if num[1] %}
      <span class="numwin">{{ "%02d" |format(num[0]) }}</span>
    {% else %}
      <span class="num">{{ "%02d" |format(num[0]) }}</span>
    {% endif %}
  {% endfor %}
  {% if match.pb[1] %}
    <span class="pbwin">{{ "%02d" |format(match.pb[0]) }}</span>
  {% else %}
    <span class="pb">{{ "%02d" |format(match.pb[0]) }}</span>
  {% endif %}
  </div>
{% endfor %}
</body></html>""")
print template.render(date1=date1, winning1=winning1, date2=date2, winning2=winning2, matches1=matches1, matches2=matches2)
