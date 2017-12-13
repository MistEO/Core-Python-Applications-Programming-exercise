import re

lm = ['Tom D', 'Div A', 'Alice,B']
ln = ['Tom Aa', 'Div Bb', "Alice Cc", 'Avs', 'Tina-Ba', 'alice Bo']

for i in lm+ln:
    print(i, re.match('[A-Z][a-z]+[ ,][A-Z]$', i))
