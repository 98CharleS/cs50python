import re

cc = input("camelCase: ")

cc_strip = re.split('(?<=.)(?=[A-Z])', cc)

n = len(cc_strip)

m = 0

print(cc_strip[0].lower(), end="")
for a in range(n-1):
    print("_"+cc_strip[m+1].lower(), end="")
    m = m + 1
