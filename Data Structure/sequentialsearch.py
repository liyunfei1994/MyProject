def sequentialsearch(alist, item):

    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

testlist = [10, 20, 23, 18, 98, 34]
print(sequentialsearch(testlist, 10))
