n = int(input())
a = 0
for i in range(1, n+1):
    # print(i)
    if i %400==0:
        a+=1
        continue
    if i % 100==0:
        continue
    if i%4==0:
        a+=1


print(a)