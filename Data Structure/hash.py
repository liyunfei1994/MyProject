def hash(astring,  tablesize):

    sum = 0
    for pos in range(len(astring)):
        print("字符是%s, ascii值为%d" % (astring[pos], ord(astring[pos])))
        sum += ord(astring[pos])

    print("和是%d, 集合的长度为%d" % (sum, tablesize))
    mod = sum % tablesize
    print("余数是%d" % mod)
    return mod


print(hash("cat", 5))


字符是c, ascii值为99
字符是a, ascii值为97
字符是t, ascii值为116
和是312, 集合的长度为5
余数是2
2
