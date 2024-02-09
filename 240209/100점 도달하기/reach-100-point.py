n = int(input())

for i in range(n, 101):
    if n < 60:
        print('F', end = ' ')
    elif n < 70:
        print('D', end = ' ')
    elif n < 80:
        print('C', end = ' ')
    elif n < 90:
        print('B', end = ' ')
    else:
        pritn('A', end = ' ')