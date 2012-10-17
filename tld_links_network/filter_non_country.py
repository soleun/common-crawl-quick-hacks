#!/usr/bin/env python
import sys
for line in sys.stdin:
    fd, td, count = line.strip().split("\t")
    if len(fd) >= 3 and len(td) >= 3:
        sys.stdout.write(line)
