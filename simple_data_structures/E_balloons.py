import sys
balls = list(map(int, sys.stdin.readline().strip().split()))

n = balls[0]
stack = []
removed = 0
color_removed = None

for ball in balls[1:]:
    if not stack:
        stack.append([ball, 1])
    elif stack and stack[-1][0] == ball:
        stack[-1][1] += 1
        if color_removed and stack[-1][0] != color_removed:
            color_removed = None
    elif stack and stack[-1][0] != ball:
        stack.append([ball, 1])
        if color_removed and stack[-1][0] != color_removed:
            color_removed = None
    if stack[-1][0] == color_removed:
        removed += stack[-1][1]
        stack.pop()
    elif stack[-1][1] == 3:
        removed += stack[-1][1]
        color_removed = stack[-1][0]
        stack.pop()

print(removed)
