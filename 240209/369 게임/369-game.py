n = int(input())

for i in range(1, n + 1):
    if i//100 ==3 or i//100==6 or i//100==9 or (i%100)//10==3 or (i%100)//10==6 or (i%100)//10==9 or i%10==3 or i%10==6 or i%10==9 or i%3 ==0:
        print(0, end = ' ')
    else:
        print(i, end = ' ')