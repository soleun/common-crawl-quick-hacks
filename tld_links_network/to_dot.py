#!/usr/bin/env python
import sys
edges = []
nodes = set()
for line in sys.stdin:
    fd, td, count = line.strip().split("\t")
    edges.append((fd,td,count))
    nodes.add(fd)
    nodes.add(td)

print "digraph {"
#print "node %s;" % ("; ".join(nodes))
for fd, td, count in edges:
    print "%s -> %s;" % (fd, td) # , count)
print "}"
    
