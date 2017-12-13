import re

lm = ['abc', '__fsfa__', '_df', 'Adsf', 'f2']
ln = ['#ds', '2f', 'dou-ds']

for i in lm+ln:
    print(i, re.match('[A-Za-z_][A-Za-z_0-9]+$', i))
