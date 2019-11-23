import re
d = {}
f = "elo.txt"
file = open(f, "r")

for line in file.read().split():
    line = line.strip().lower()
    line = re.sub(r'[^\w\s]','',line)
    if not(line in d):
        d[line] = 1
    else:
        num = d[line] + 1
        d.update({line: num})

for key in d: 
    print(key, ":", d[key]) 

# for key, value in d.items():
#         print(f"\nWord: {key}")
#         print(f"Occurrences: {value}")