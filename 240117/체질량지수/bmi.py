a, b = map(int, input().split())

a /= 100

print(int(b/(a**2)))

if b/(a**2) > 25:
    print('Obesity')