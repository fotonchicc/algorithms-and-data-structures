def count_postfix(expression):
    stack = []
    for char in expression:
        if not char.isspace():
            if char.isdigit():
                stack.append(int(char))
            else:
                second_element = stack.pop()
                first_element = stack.pop()
                formula = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y
                }[char]
                result = formula(first_element, second_element)
                stack.append(result)
    return stack


numeric_expression = input()
res = count_postfix(numeric_expression)
print(*res)
