#!/usr/bin/python3
with open('new.txt') as f:
     lines = f.read().splitlines()
     lenth = len(lines)
     print(lines)
     print(lenth)
     count = {}
     for line in lines:
#      count[line]=count.get(line,0)+1
#      print(count)
      try:
         count[line] += 1
      except:
            count[line] = 1
     for k,v in count.items():
      print("{} : {}".format(k.strip(),v))
