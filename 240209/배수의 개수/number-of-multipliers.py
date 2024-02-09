a = 0
b = 0

for i in range(10):
    c = int(input())

    if c%3==0:
        a+=1
    if c%5==0:
        b+=1
print(a, b)