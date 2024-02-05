aa, ag = input().split()

ba, bg = input().split()

aa = int(aa)
ba = int(ba)

if (ba>=19 and bg == 'M') or (aa>= 19 and ag =='M'):
    print(1)
else:
    print(0)