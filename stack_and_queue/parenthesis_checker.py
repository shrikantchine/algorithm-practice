def parenthesis_checker(s):
    openining = ['{', '[', '(']
    closing = ['}', ']', ')']

    stack = []

    for i, val in enumerate(s):
        if val in openining:
            stack.append(val)
        elif val in closing and len(stack) == 0:
            return False
        elif val in closing:
            last_opened = stack.pop()
            if last_opened != openining[closing.index(val)]:
                return False
        else:
            pass # Ignore other characters

    return True

assert parenthesis_checker('{([])}') == True
assert parenthesis_checker('()') == True
assert parenthesis_checker('(]') == False