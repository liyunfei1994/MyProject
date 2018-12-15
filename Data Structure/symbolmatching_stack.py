import stack

def parchecker(symbolstring):
    s = stack.Stack()
    balanced =True
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parchecker('(()))'))
# False
print(parchecker('(()())'))
# True
