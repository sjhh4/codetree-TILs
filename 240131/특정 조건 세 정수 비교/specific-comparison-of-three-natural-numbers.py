a, b, c = map(int, input().split())

if a == min(a, b, c):
    d = 1
else:
    d = 0

if a == b == c:
    e = 1
else:
    e = 0

print(d, e)