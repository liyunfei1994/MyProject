def ordersearch(alist, item):

    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:

        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found

testlist = [10, 20, 25, 30, 40, 48]
print(ordersearch(testlist, 29))
