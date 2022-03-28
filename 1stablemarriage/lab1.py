import sys
import time
start = time.time()

debug = False

if debug:
    inp_file = "data/secret/4testhuge.in"
    with open(inp_file, 'r') as f:
        lines = f.read().splitlines()
    n = int(lines[0])
    oneline = [int(item)-1 for sublist in lines[1:] for item in sublist.split(" ")]
else:
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

# i:th list member contains the index of the man the ith woman is paired with
ret = [-1 for _ in range(n)]  # -1 indicates being available

freemen = [i for i in range(n)]
while len(freemen) > 0:
    if debug and len(freemen)%(n/10)==0:
        print(f"{len(freemen)} men left to pair")
    # Find index of first free man
    m = freemen[0]

    for w in men[m]: # Go through man's preference in women in order
        if ret[w] == -1:
            ret[w] = m
            freemen.remove(m)
            break
        else: # w is already paired with some other man, m2
            m2 = ret[w]
            if women[w].index(m) < women[w].index(m2):
                ret[w] = m
                freemen.remove(m)
                freemen.append(m2)
                break

[print(num+1) for num in ret]

if debug:
    print(f"{time.time()-start}s")