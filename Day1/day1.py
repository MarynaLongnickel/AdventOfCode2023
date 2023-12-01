# --- Trebuchet?! ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfcode2023/main/Day1/day1.txt').read().decode().split('\n')

def day1(l):
    ans = 0

    for s in s2:
        d = []
        while len(s) > 0:
            if len(s) == 0:
                break
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
                # print(s, s[:len(n)], n, d)
            if not found:
                s = s[1:]
        ans += int(d[0] + d[-1])
    print(ans)

# ---------------------- PART 1 ------------------------

day1(list(m.values()))

# ---------------------- PART 2 ------------------------

day1(list(m.keys()) + list(m.values()))
