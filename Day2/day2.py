# --- Cube Conundrum ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day2/day2.txt').read().decode().split('\n')[:-1]
games = [y.split('; ') for y in [x.split(': ')[1] for x in data]]

# ---------------------- PART 1 ------------------------

ans = []

for i in range(len(games)):
    
    d = {'red': 0, 'green': 0, 'blue': 0}
    fail = False
    
    game = games[i]
    for s in game:
        if fail:
            break
        s.split(' ')
        for cube in s.split(', '):
            if fail:
                break
            n, c = cube.split(' ')
            d[c] = int(n)
            if d['red'] > 12 or d['green'] > 13 or d['blue'] > 14:
                fail = True
                break       
            
    if not fail:
        ans.append(i+1)
    
print(sum(ans))

# ---------------------- PART 2 ------------------------

ans = []

for game in games:
    
    d = {'red': 0, 'green': 0, 'blue': 0}

    for s in game:
        s.split(' ')
        for cube in s.split(', '):
            n, c = cube.split(' ')
            if int(n) > d[c]:
                d[c] = int(n)
    ans.append(d['red'] * d['green'] * d['blue'])
        
print(sum(ans))
