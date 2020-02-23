#!/usr/bin/python3

import sys
import string

data = sys.stdin.read()

limit = 1
sed_len = 9

chars = string.digits + string.ascii_letters
subs = list()

# Keep chars that don't exist
for c in list(chars):
  if c not in data:
    subs.append(c)

print("We will use there chars to compress:")
print(subs)

sed_pre = "s/^.* #//;"
sed_post = " #"
sed = ""

def compressed(string, mark):
  pats = set()
  for i in range(1, int((len(string)-1))):
    for j in range(1, int((len(string)-i))):
      if (i + j) <= len(string):
        pats.add(string[i:i+j])

  bests = 0
  bestp = ""
  for p in pats:
    c = string.count(p)
    saved = (c*(len(p) - 1)) - (sed_len + len(p))
    if saved > bests:
      bests = saved
      bestp = p

  #print("Best p: %s (saves %d)" % (bestp, bests))
  return(bestp, bests)

for s in subs:
  (pat, saved) = compressed(data, s)
  if saved < limit:
    break
  data = data.replace(pat, s)
  pat = pat.replace("\\","\\\\")
  sed = ("s/%s/%s/g;" % (s, pat)) + sed
  print("Shrank: %d bytes" % (saved))
  output = sed_pre + sed + sed_post + data
  print(output)
  print("")

