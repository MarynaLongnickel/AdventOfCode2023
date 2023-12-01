# --- Trebuchet?! ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day1/day1.txt').read().decode().split('\n')[:-1]

m = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def day1(l):
    ans = 0
    found = False

    for s in data:
        d = []
        while len(s) > 0:
            for n in l:
                found = False
                if len(s) == 0:
                    break
                if s[:len(n)] == n:
                    if len(n) == 1:
                        s = s[len(n):]
                        d.append(n)
                    else:
                        s = s[len(n) - 1:]
                        d.append(m[n])
                    found = True
                    break
            if not found:
                s = s[1:]
        ans += int(d[0] + d[-1])
    print(ans)

# ---------------------- PART 1 ------------------------

day1(m.values())

# ---------------------- PART 2 ------------------------

day1(list(m.keys()) + list(m.values()))
