am, ae = map(int, input().split())
bm, be = map(int, input().split())

if am>bm:
    print('A')
elif bm>am:
    print('B')
else:
    if ae>be:
        print('A')
    elif be>ae:
        print('B')
    else:
        pass