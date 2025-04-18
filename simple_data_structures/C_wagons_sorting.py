import sys

lst_in = [list(map(int, value.split())) for value in list(map(str.strip, sys.stdin.readlines()))]
n = lst_in[0][0]
path_1 = lst_in[1]
deadlock = []
path_2 = []
resp = []
while len(path_2) != n:
    if path_1:
        if not deadlock or deadlock[-1] > path_1[0]:
            deadlock.append(path_1.pop(0))
            resp.append('1 1')
        elif deadlock[-1] < path_1[0]:
            if not path_2:
                path_2.append(deadlock.pop(-1))
                resp.append('2 1')
            else:
                if (path_2[-1] < deadlock[-1]) and (deadlock[-1] - path_2[-1] == 1):
                    path_2.append(deadlock.pop(-1))
                    resp.append('2 1')
                else:
                    print(0)
                    break
    else:
        if not path_2:
            path_2.append(deadlock.pop(-1))
            resp.append('2 1')
        elif (path_2[-1] < deadlock[-1]) and (deadlock[-1] - path_2[-1] == 1):
            path_2.append(deadlock.pop(-1))
            resp.append('2 1')
        elif path_2[-1] > deadlock[-1]:
            print(0)
            break
else:
    for item in resp:
        print(item)
