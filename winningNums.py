#!/usr/bin/python

from urllib import urlopen
from HTMLParser import HTMLParser

class MMParser(HTMLParser):
    results = []
    target = None
    pending = []
    def handle_starttag(self, tag, attrs):
        if (tag == 'td'):
            for attr in attrs:
                if (attr[0] == 'class' and attr[1] == 'dates'):
                    self.target = 1
                elif (attr[0] == 'class' and attr[1] == 'details'):
                    self.results.append((self.pending[0], self.pending[1:6], self.pending[6]))
                    self.target = None
                    self.pending = []
    def handle_data(self, data):
        if (self.target):
            data = data.strip()
            if (data != ''):
                self.pending.append(data)
    def getNums(self, days=1):
        return self.results[0:days]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data

def getWinning(days=1):
    url = urlopen('http://megamillions.com/winning-numbers/last-25-drawings')
    parser = MMParser()
    for line in url:
        parser.feed(line)
    parser.close()
    return parser.getNums(days)

if __name__ == "__main__":
    winning = getWinning(2)
    print winning
