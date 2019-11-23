d = {}
f = "elo.txt"
file = open(f, "r")

for str in file.read().split():
    if not(str in d):
        d[str] = 1
    else:
        num = d[str] + 1
        d.update({str: num})

for key, value in d.items():
        print(f"\nWord: {key}")
        print(f"Occurrences: {value}")