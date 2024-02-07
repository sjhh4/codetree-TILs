a, b = map(int, input().split())

for i in range(min(a, b), max(a, b)+1):
    if i % 2 == 1:
        print(i , end = ' ')