# --- Day 4: Scratchcards ---

from urllib.request import urlopen
import regex as re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day4/day4.txt').read().decode().split('\n')[:-1]
cards = [x.split(':')[1].replace('  ', ' ').split(' | ') for x in data]
nums = [re.findall(r'\d+', c) for card in cards for c in card]
points = [len(list(set(nums[i]).intersection(set(nums[i+1])))) for i in range(0, len(nums) - 1, 2)]
      
# ---------------------- PART 1 ------------------------
sum([2**(x-1) if x > 0 else 0 for x in points])

# ---------------------- PART 2 ------------------------
ans = [1] * len(cards)

for i in range(len(ans)):
    w = points[i]
    for j in range(i+1, i + 1 + w):
        ans[j] += ans[i]

sum(ans)
