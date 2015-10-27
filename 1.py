__author__ = 'Administrator'

import urllib2
from bs4 import BeautifulSoup
import codecs

url = 'http://www.bloomberg.com/asia'


if __name__ == "__main__":
    bg = urllib2.urlopen(url).read()
    soup = BeautifulSoup(bg)
#   print soup.prettify().encode('utf-8')
#   soup.find(), soup.find_all('a'), soup.find_all(re.compile('t'))
