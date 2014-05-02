import sys
import re

NONWORD_RE = re.compile('\W+')
print NONWORD_RE
idx = {}
with open(sys.argv[1]) as fp:
    for n, line in enumerate(fp, 1):
        print fp
        for word in NONWORD_RE.split(line):
            if word.strip():
                idx.setdefault(word, []).append(n)

for word in sorted(idx, key=str.upper):
    pass
    #print (word, idx[word])
