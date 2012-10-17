#!/usr/bin/env python
import sys, math

edges = []
nodes = set()
for line in sys.stdin:
    fd, td, count = line.strip().split("\t")
    edges.append((fd,td,count))
    nodes.add(fd)
    nodes.add(td)

emitted_node = set()
print "graph ["
for fd, td, count in edges:

    # since gephi cant handle self edges lets hackily convert x -> x to _x -> x
    if fd == td:
        fd = "_" + fd  

    if not fd in emitted_node:
        print "node [ id %s label \"%s\" ]" % (fd, fd)
        emitted_node.add(fd)
    if not td in emitted_node:
        print "node [ id %s label \"%s\" ]" % (td, td)
        emitted_node.add(td)
    print "edge [ source %s target %s value %s ]" % (fd, td, math.log10(float(count)))

print "]"
    
