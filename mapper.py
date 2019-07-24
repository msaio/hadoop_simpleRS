#!/usr/bin/python


import sys

for line in sys.stdin:
	line = line.strip()
	for char in '-.,"!@%?;\n':
		line = line.replace(char,'')
	line = line.lower()
	words = line.split()
	for word in words:
		print'%s\t%s' % (word,1)
