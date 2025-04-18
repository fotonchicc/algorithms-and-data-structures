import sys

lst_in = [list(map(int, value.split())) for value in list(map(str.strip, sys.stdin.readlines()))]
stack = []
n = lst_in[0][0] + 1
for value in lst_in[1:n]:
    operation = value[0]
    if operation == 1:
        val = value[1]
        if not stack or stack[-1][1] > val:
            stack.append((val, val))
        elif stack[-1][1] <= val:
            stack.append((val, stack[-1][1]))
    elif operation == 2:
        if stack:
            stack.pop()
    elif operation == 3:
        if stack:
            print(stack[-1][1])
