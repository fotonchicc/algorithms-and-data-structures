import sys
lst_in = [list(map(int, value.split())) for value in list(map(str.strip, sys.stdin.readlines()))]
queue = [None]*(10**5+1)
queue2 = []
l = 0
k = 0
p = 0
for i in lst_in[1:]:
    oper = i[0]
    if oper == 1:
        queue[i[1]] = k
        queue2.append(i[1])
        k+=1
    elif oper == 2: l+=1
    elif oper == 3:
        queue2.pop(-1)
        k-=1
    elif oper == 4:
        print(queue[i[1]]-l)
    else:
        print(queue2[l])
