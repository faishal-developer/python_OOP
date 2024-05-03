s = """}"""
stack = []
result = True

for value in s:
    if (value == "(") or (value == "[") or (value == "{"):
        stack.append(value)
    elif len(stack) == 0:
        result = False
        break
    elif value == ")":
        if stack[-1] == "(":
            stack.pop()
        else:
            result = False
            break
    elif value == "}":
        if stack[-1] == "{":
            stack.pop()
        else:
            result = False
            break
    elif value == "]":
        if stack[-1] == "[":
            stack.pop()
        else:
            result = False
            break

if len(stack) >= 1:
    print(False)
else:
    print(result)
