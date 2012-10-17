#!/usr/bin/env python
import sys
from collections import Counter

counts = Counter()

for line in sys.stdin:
    uf, ut, count = line.strip().split("\t")
    counts[(uf, ut)] += int(count)

for (uf, ut), count in counts.iteritems():
    print "%s\t%s\t%s" % (uf, ut, count)
