def binarysearch(alist, item):
    first =0
    last = len(alist) - 1
    found = False

    while first <= last and not  found:
        print("移动之前first=%d, last=%d" % (first, last))
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True

        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

        print("移动之后first=%d, last=%d" % (first, last))

        print("中点是",midpoint)

    return found


testlist = [1, 2, 8, 15, 19, 23, 34, 40]
print(binarysearch(testlist, 25))

移动之前first=0, last=7
移动之后first=4, last=7
中点是 3
移动之前first=4, last=7
移动之后first=6, last=7
中点是 5
移动之前first=6, last=7
移动之后first=6, last=5
中点是 6
False
