#!/usr/bin/env python
import sys
from collections import Counter

# slurp valid tlds
# wget http://data.iana.org/TLD/tlds-alpha-by-domain.txt
valid_tlds = set([x.strip().lower() \
                  for x in open("tlds-alpha-by-domain.txt", 'r').readlines()])

def tld_of(domain):
    return domain.split(".")[-1]

c = Counter()

flush_rate = int(sys.argv[1])
valid = invalid = 0
for line in sys.stdin:
    from_domain, to_domain, freq = line.strip().lower().split()
    from_tld, to_tld = map(tld_of, [from_domain, to_domain])

    if from_tld in valid_tlds and to_tld in valid_tlds:
        valid += 1
        c[(from_tld, to_tld)] += 1
    else:
        invalid += 1

    if valid > flush_rate:
        print >>sys.stderr, "#valid=%s #invalid=%s" % (valid, invalid)
        for (f, t), count in c.iteritems():
            print "\t".join([f, t, str(count)])
        c.clear()
        valid = invalid = 0

# final
print >>sys.stderr, "#valid=%s #invalid=%s" % (valid, invalid)
for (f, t), count in c.iteritems():
    print "\t".join([f, t, str(count)])
