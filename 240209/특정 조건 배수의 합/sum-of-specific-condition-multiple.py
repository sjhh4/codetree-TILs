a, b= map(int, input().split())
answer = 0
for i in range(min(a, b), max(a, b)+1):
    if i%5==0:
        answer += i

print(answer)