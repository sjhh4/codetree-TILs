a = list(input().split())
b = list(input().split())
c = list(input().split())

patients = [a, b, c]

e = []
for i in range(3):
    patients[i][1] = float(patients[i][1])
# print(patients)
A = 0
B = 0
C = 0
D = 0
for i in range(len(patients)):
    if patients[i][0] == 'Y':
        if patients[i][1] >= 37:
            A +=1
        else:
            C += 1
    else:
        if patients[i][1] >= 37:
            B += 1
        else:
            D += 1

if A >= 2:
    print('E')
else:
    print('N')