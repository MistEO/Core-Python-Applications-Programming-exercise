import re

lm = ['Tom Aa', 'Div Bb', "Alice Cc"]
ln = ['Avs', 'Tina-Ba', 'alice Bo']

for i in lm+ln:
    print(i, re.match('[A-Z][a-z]+ [A-Z][a-z]+', i))
