import stack

# 转换为2进制，base就是2，转换成16进制，base就是16
def baseconverter(number, base):
    digits = "0123456789ABCDEF"

    remstack = stack.Stack()
    while number>0:
        rem = number % base
        remstack.push(rem)
        number = number // base

    newstring = ""
    while not remstack.isEmpty():
        newstring += digits[remstack.pop()]

    return newstring


print(baseconverter(28, 16))
# 1C
