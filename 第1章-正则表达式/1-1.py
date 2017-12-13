import re

l = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']

for i in l:
    print(re.match('[bh][iau]t', i))
