a, b = map(int, input().split())

for i in range(max(a, b), min(a, b)-1, -1):
    print(i, end = ' ')