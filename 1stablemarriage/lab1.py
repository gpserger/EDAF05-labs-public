import sys
import time
start = time.time()

debug = True

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

# Dictionary of all men and women's preferences by ID

# for line in lines[1:]:
#     i, pref = int(line[0])-1, [int(num)-1 for num in line[1:].split()]
#     if i not in women:
#         women[i] = pref
#     else:
#         men[i] = pref

# i:th list member contains the index of the man the ith woman is paired with
ret = [-1 for _ in range(n)]  # -1 indicates being available

# If there is -1 in the array, there is a single woman, which means there is also a single man
while -1 in ret:
    # Find index of first free man
    m = -1
    for i in range(n):
        if i not in ret:
            m = i
            break

    for w in men[m]: # Go through man's preference in women in order
        if ret[w] == -1:
            ret[w] = m
            break
        else: # w is already paired with some other man, m2
            m2 = ret[w]
            if women[w].index(m) < women[w].index(m2):
                ret[w] = m
                break


# while -1 in ret:
#     w = ret.index(-1)  # index of the first available woman
#     for m in women[w]:  # Next highest ranked person on w's list
#         if m not in ret:
#             ret[w] = m
#             break
#         else: # m is already paired with some other woman, w2
#             w2 = ret.index(m)
#             if men[m].index(w) < men[m].index(w2):
#                 ret[w] = m
#                 break



[print(num+1) for num in ret]

if debug:
    print(f"{time.time()-start}s")