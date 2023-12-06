# --- Day 6: Wait For It ---

from urllib.request import urlopen
import regex as re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day6/day6.txt').read().decode().split('\n')[:-1]

times, distances = [x.split()[1:] for x in data]
time = list(map(int, times))
dist = list(map(int, distances))
      
# ---------------------- PART 1 ------------------------

tot = 1

for i in range(len(time)):
    c = 0
    for t in range(time[i]):
        tt = t + t * (time[i] - t)
        if t * (time[i] - t) > dist[i]:
            c += 1
    tot *= c
    
print(tot)

# ---------------------- PART 2 ------------------------

time2 = int(''.join(times))
dist2 = int(''.join(distances))

c = 0
for t in range(time2):
    tt = t + t * (time2 - t)
    if t * (time2 - t) > dist2:
        c += 1
      
print(c)
