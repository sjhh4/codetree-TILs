n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    if number%2==1 and number%3==0:
        print(number)