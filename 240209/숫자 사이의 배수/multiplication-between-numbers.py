a, b = map(int, input().split())
answer=0

number =0
for i in range(a, b+1):
    if i %5==0 or i%7==0:
        answer += i
        number += 1
print(f'{answer} {answer/number:.1f}')