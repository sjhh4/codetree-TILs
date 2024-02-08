a, b = map(int, input().split())

print(f'{a//b}.', end = '')
a %= b
for i in range(1, 21):
    a *= 10
    print(f'{a//b}', end = '')
    a %= b