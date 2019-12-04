import re
d = {}
f = "files/praca2.txt"
file = open(f, "r")

for line in file.read().split():
    line = line.lower().strip()
    line = re.sub(r'[^A-Za-z0-9]+','',line)
    if not(line in d):
        d[line] = 1
    else:
        num = d[line] + 1
        d.update({line: num})

for key, value in sorted(d.items(), key=lambda d: d[1], reverse=False): #Swap to True, to reverse order
    print(f"\nSłowo: {key}")
    print(f"Liczba wystąpień: {value}")