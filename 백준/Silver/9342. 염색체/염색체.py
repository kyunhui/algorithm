import sys
input = sys.stdin.readline

valid = set("ABCDEF")

def is_infected(s: str) -> bool:
    n = len(s)
    for start in (0, 1):
        i = start
        if start == 1:
            if n == 0 or s[0] not in valid:
                continue

        if i >= n or s[i] != 'A':
            continue
        while i < n and s[i] == 'A':
            i += 1

        if i >= n or s[i] != 'F':
            continue
        while i < n and s[i] == 'F':
            i += 1

        if i >= n or s[i] != 'C':
            continue
        while i < n and s[i] == 'C':
            i += 1

        if i == n:
            return True
        if i == n - 1 and s[i] in valid:
            return True
    return False

t = int(input())
for _ in range(t):
    s = input().strip()
    print("Infected!" if is_infected(s) else "Good")