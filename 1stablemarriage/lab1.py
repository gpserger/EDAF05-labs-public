import sys
import time

# type .\data\sample\2.in | python3 .\lab1.py

start = time.time()

debug = False

if debug:
    # read input from specific file
    inp_file = "data/secret/4testhuge.in"
    with open(inp_file, 'r') as f:
        lines = f.read().splitlines()
    n = int(lines[0])
    oneline = [int(item)-1 for sublist in lines[1:] for item in sublist.split(" ")]
else:
    # read input from stdin
    lines = []
    for line in sys.stdin:
        lines.append(line.rsplit())
    n = int(lines[0][0])
    oneline = [int(item)-1 for sublist in lines[1:] for item in sublist]


# Make preference dictionaries
men, women = dict(), dict()
for i in range(2*n):
    index = i*(n+1)
    key = oneline[index]
    if key not in women:
        women[key] = oneline[index+1:index+1+n]
    else:
        men[key] = oneline[index+1:index+1+n]

# i:th list member contains the index of the man the ith woman is paired with, which is the intended ouput format
result = [-1 for _ in range(n)]  # -1 indicates being available

if debug:
    print(f"{time.time()-start}s")

singlemen = [i for i in range(n)]

# Run while there are single m
while len(singlemen) > 0:
    if debug and len(singlemen)%(n / 10)==0:
        print(f"{len(singlemen)} men left to pair")

    # Find id of first free m
    m = singlemen[0]

    for w in men[m]:  # Go through m's preference in ws in order
        if result[w] == -1:
            # If w is single, pair them up
            result[w] = m
            singlemen.remove(m)
            break
        else:
            # w is already paired with someone else: m2
            m2 = result[w]
            if women[w].index(m) < women[w].index(m2):
                # If w prefers m over m2, pair them up and make m2 single again
                result[w] = m
                singlemen.remove(m)
                singlemen.append(m2)
                break

# Everyone is paired so print the result
[print(num+1) for num in result]

if debug:
    print(f"{time.time()-start}s")