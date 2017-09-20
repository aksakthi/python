#!/usr/bin/python
import chain
with open("new.txt") as input_file:
  print list(chain.from_interable(line.split() for line in input_file))
