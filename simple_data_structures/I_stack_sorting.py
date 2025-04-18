import sys

lst_in = [list(map(int, value.split())) for value in list(map(str.strip, sys.stdin.readlines()))]
n = lst_in[0][0]
A = lst_in[1]
B = []
num = 1
resp = []
while A or B:
    if len(A) > 1:
        if not B:
            B.append(A.pop(0))
            resp.append('push')
        elif B[-1] == num:
            B.pop(-1)
            resp.append('pop')
            num += 1
        elif A[0] > A[1] or A[0] == num:
            B.append(A.pop(0))
            resp.append('push')
        else:
            print('impossible')
            break
    elif A:
        if not B or A[0] == num:
            B.append(A.pop(0))
            resp.append('push')
        elif B[-1] == num:
            B.pop(-1)
            resp.append('pop')
            num += 1
        else:
            print('impossible')
            break
    else:
        if B[-1] == num:
            B.pop(-1)
            resp.append('pop')
            num += 1
        else:
            print('impossible')
            break
else:
    for item in resp:
        print(item)
