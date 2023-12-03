# --- Gear Ratios ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day3/day3.txt').read().decode().split('\n')[:-1]
chars = ''.join(sorted([x for x in list(set(''.join(data))) if not x.isnumeric() and x!= '.']))

nums = 0
gears = {}

def get_ans(nums):

    if n != '':
        if any(c in chars for c in box):
            nums += int(n)
            
        if '*' in top:
            gc = max(0, x - 1) + top.index('*')
            gi = (i-1, gc)
        if '*' in middle:
            gc = max(0, x - 1) + middle.index('*')
            gi = (i, gc)
        if '*' in bottom:
            gc = max(0, x - 1) + bottom.index('*')
            gi = (i+1, gc)

        if '*' in top or '*' in middle or '*' in bottom:
            if gi not in gears.keys():
                gears[gi] = []
            gears[gi].append(int(n))
    return nums
        

for i in range(len(data)):
    row = data[i]
    x = 0
    n = ''
    
    for j in range(len(row)):
        top = data[i-1][max(0, x-1):min(x+len(n)+1, len(data[0]))] if i > 0 else ''
        middle = data[i][max(0, x-1):min(x+len(n)+1, len(data[0]))]
        bottom = data[i+1][max(0, x-1):min(x+len(n)+1, len(data[0]))] if i < len(data) - 1 else ''
        box = top + middle + bottom
        box = ''.join(box)
        
        if row[j].isnumeric():
            if x == 0 and n == '':
                x = j
            n += row[j]
        else:
            nums = get_ans(nums)
            x = 0
            n = ''
            
        if j == len(row)-1:
            nums = get_ans(nums)
            
ratios = 0

for k, ns in gears.items():
    if len(ns) == 2:
        ratios += ns[0] * ns[1]
      
# ---------------------- PART 1 ------------------------
print(nums)

# ---------------------- PART 2 ------------------------
print(ratios)
