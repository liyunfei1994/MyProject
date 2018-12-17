import stack

def divideby2(number):
    remstack = stack.Stack()

    while number >0:
        rem = number % 2
        remstack.push(rem)
        number  = number // 2

    binstring = ""
    while not remstack.isEmpty():
        binstring += str(remstack.pop())

    return binstring


print(divideby2(23))
# 10111
