#!/usr/bin/python3

import sys
import string

# Read all the data
data = sys.stdin.read()

limit = 1
sed_len = 9
markers = list()
orig_len = len(data)

# Keep chars that don't exist
chars = string.digits + string.ascii_letters
for c in list(chars):
    if c not in data:
        markers.append(c)

# Check that we have any markers left (or fail)
if len(markers) <= 1:
  print("Not enough unused chars in input to do anything useful. :(")
  sys.exit(1)

if data.find("\n") != -1:
    c = markers.pop(0)
    data = data.replace("\n", c)
    sed_post = "y/" + c + "/\\n/;"
else:
    sed_post = ""

print("We will use these chars as markers:")
print(''.join(markers))

if data.find("#") != -1:
    sed_pre = "s/^.* #" + markers[0]+ "//;"
    sed_post += " #" + markers[0]
else:
    sed_pre = "s/^.* #//;"
    sed_post += " #"

sed = ""

def compressed(string):
    bests = 0
    bestp = ""
    # Find the substring that will save the most space
    for i in range(1, int((len(string)-2))):
        for j in range(2, int((len(string)-i)/2)):
            if (i + j) <= len(string):
                p = string[i:i+j]
                c = string.count(p)
                saved = (c*(len(p) - 1)) - (sed_len + len(p))
                if saved > bests:
                    bests = saved
                    bestp = p
    return(bestp, bests)

# As long as we have markers, find a substring to replace
for m in markers:
    (pat, saved) = compressed(data)
    # ...actually, if we don't same enough, just give up.
    if saved < limit:
        break
    data = data.replace(pat, m)
    m = m.replace('\\', '\\\\')
    m = m.replace('/', '\/')
    m = m.replace('&', '\&')
    pat = pat.replace('\\', '\\\\')
    pat = pat.replace('/', '\/')
    pat = pat.replace('&', '\&')
    sed = ("s/%s/%s/g;" % (m, pat)) + sed
    print("Shrank: %d bytes" % (saved))
    output = sed_pre + sed + sed_post + data
    print(output)
    print("")

print("Original length: %d" % (orig_len))
print("Final length: %d (%d)" % (len(output), len(data)))
