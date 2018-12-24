def bubblesort(alist):

    count = 1
    for passnum in range(len(alist)-1, 0, -1):
        # print("len(alist)-1 ", len(alist)-1)
        print("第%d轮遍历" % count)
        print("passnum为", passnum)
        for i in range(passnum):
            print("i为", i)

            print("要进行交换吗？ %s" % ("Yes" if alist[i]>alist[i+1] else "No"))
            if alist[i] > alist[i + 1]:
                print("alist[%d] = %d, alist[%d + 1] = %d" %
                      (i, alist[i], i, alist[i + 1]))
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                print("交换之后，alist[%d]=%d, alist[%d+1]=%d" %
                      (i, alist[i], i, alist[i+1]))
            print()
        count += 1
        print("新的list为",alist)
        print()


bbb = [54, 25, 96, 33, 70, 13, 19]
print(bbb)
print()
bubblesort(bbb)
print(bbb)


[54, 25, 96, 33, 70, 13, 19]

第1轮遍历
passnum为 6
i为 0
要进行交换吗？ Yes
alist[0] = 54, alist[0 + 1] = 25
交换之后，alist[0]=25, alist[0+1]=54

i为 1
要进行交换吗？ No

i为 2
要进行交换吗？ Yes
alist[2] = 96, alist[2 + 1] = 33
交换之后，alist[2]=33, alist[2+1]=96

i为 3
要进行交换吗？ Yes
alist[3] = 96, alist[3 + 1] = 70
交换之后，alist[3]=70, alist[3+1]=96

i为 4
要进行交换吗？ Yes
alist[4] = 96, alist[4 + 1] = 13
交换之后，alist[4]=13, alist[4+1]=96

i为 5
要进行交换吗？ Yes
alist[5] = 96, alist[5 + 1] = 19
交换之后，alist[5]=19, alist[5+1]=96

新的list为 [25, 54, 33, 70, 13, 19, 96]

第2轮遍历
passnum为 5
i为 0
要进行交换吗？ No

i为 1
要进行交换吗？ Yes
alist[1] = 54, alist[1 + 1] = 33
交换之后，alist[1]=33, alist[1+1]=54

i为 2
要进行交换吗？ No

i为 3
要进行交换吗？ Yes
alist[3] = 70, alist[3 + 1] = 13
交换之后，alist[3]=13, alist[3+1]=70

i为 4
要进行交换吗？ Yes
alist[4] = 70, alist[4 + 1] = 19
交换之后，alist[4]=19, alist[4+1]=70

新的list为 [25, 33, 54, 13, 19, 70, 96]

第3轮遍历
passnum为 4
i为 0
要进行交换吗？ No

i为 1
要进行交换吗？ No

i为 2
要进行交换吗？ Yes
alist[2] = 54, alist[2 + 1] = 13
交换之后，alist[2]=13, alist[2+1]=54

i为 3
要进行交换吗？ Yes
alist[3] = 54, alist[3 + 1] = 19
交换之后，alist[3]=19, alist[3+1]=54

新的list为 [25, 33, 13, 19, 54, 70, 96]

第4轮遍历
passnum为 3
i为 0
要进行交换吗？ No

i为 1
要进行交换吗？ Yes
alist[1] = 33, alist[1 + 1] = 13
交换之后，alist[1]=13, alist[1+1]=33

i为 2
要进行交换吗？ Yes
alist[2] = 33, alist[2 + 1] = 19
交换之后，alist[2]=19, alist[2+1]=33

新的list为 [25, 13, 19, 33, 54, 70, 96]

第5轮遍历
passnum为 2
i为 0
要进行交换吗？ Yes
alist[0] = 25, alist[0 + 1] = 13
交换之后，alist[0]=13, alist[0+1]=25

i为 1
要进行交换吗？ Yes
alist[1] = 25, alist[1 + 1] = 19
交换之后，alist[1]=19, alist[1+1]=25

新的list为 [13, 19, 25, 33, 54, 70, 96]

第6轮遍历
passnum为 1
i为 0
要进行交换吗？ No

新的list为 [13, 19, 25, 33, 54, 70, 96]

[13, 19, 25, 33, 54, 70, 96]
