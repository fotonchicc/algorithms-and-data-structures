def is_correct(sequence):
    stack = []
    is_good = True
    for char in sequence:
        if char in '{[(':
            stack.append(char)
            continue
        if not stack:
            is_good = False
            break
        open_bracket = stack.pop()
        if char == ')':
            if open_bracket == '(':
                continue
        if char == '}':
            if open_bracket == '{':
                continue
        if char == ']':
            if open_bracket == '[':
                continue
        is_good = False
        break
    res = is_good and len(stack) == 0
    if res:
        return 'YES'
    else:
        return 'NO'

sequence = input()
check_result = is_correct(sequence)
print(check_result)
