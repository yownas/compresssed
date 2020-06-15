#!/usr/bin/python3

import sys
import string

# Read all the data
data = sys.stdin.read()
data = data.strip()

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
  sys.stderr.write("Not enough unused chars in input to do anything useful. :(\n")
  sys.exit(1)

if data.find("\n") != -1:
    c = markers.pop(0)
    data = data.replace("\n", c)
    sed_post = "y/" + c + "/\\n/;"
else:
    sed_post = ""

sys.stderr.write("We will use these chars as markers:\n")
sys.stderr.write(''.join(markers))
sys.stderr.write("\n")

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
    for i in range(0, int((len(string)-2))):
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
output = None
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
    sys.stderr.write("Shrank: %d bytes\n" % (saved))
    output = sed_pre + sed + sed_post + data
    sys.stderr.write(output + "\n\n")

if output:
    sys.stderr.write("Original length: %d\n" % (orig_len))
    sys.stderr.write("Final length: %d (%d)\n" % (len(output), len(data)))
    print(output)
else:
    sys.stderr.write("Oops. Couldn't find a way to compress the input.")
