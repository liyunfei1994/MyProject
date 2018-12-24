def selectsort(alist):

    count = 1
    for fillslot in range(len(alist)-1, 0, -1):
        print("第%d次遍历" % count)
        print("此时插入的位置为", fillslot)
        # 先假设最大值的位置在0
        positionofmax = 0
        print("先假设最大值位于%d, 值为%d" %
              (positionofmax, alist[positionofmax]))
        for location in range(1, fillslot+1):
            print("此时的location为%d, 值为%d" % (location, alist[location]))
            print("是否需要修改最大值的位置-->%s " %
                  ("Yes" if alist[location]>alist[positionofmax] else "No"))
            if alist[location] > alist[positionofmax]:
                print()
                print("此时最大值的位置不是原先的%d" % positionofmax)
                positionofmax = location
                print("修改之后，最大值的位置为%d, 值为%d" %
                      (positionofmax, alist[positionofmax]))
            print()
        count += 1
        print("此时，比较完毕")
        print("将最大值%d放在%d" % (alist[positionofmax], fillslot))
        temp = alist[fillslot]
        alist[fillslot] = alist[positionofmax]
        alist[positionofmax] = temp
        print("修改之后的list为", alist)
        print()


bbb = [54, 26, 70, 24, 19, 60, 33]
selectsort(bbb)
print(bbb)


第1次遍历
此时插入的位置为 6
先假设最大值位于0, 值为54
此时的location为1, 值为26
是否需要修改最大值的位置-->No 

此时的location为2, 值为70
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的0
修改之后，最大值的位置为2, 值为70

此时的location为3, 值为24
是否需要修改最大值的位置-->No 

此时的location为4, 值为19
是否需要修改最大值的位置-->No 

此时的location为5, 值为60
是否需要修改最大值的位置-->No 

此时的location为6, 值为33
是否需要修改最大值的位置-->No 

此时，比较完毕
将最大值70放在6
修改之后的list为 [54, 26, 33, 24, 19, 60, 70]

第2次遍历
此时插入的位置为 5
先假设最大值位于0, 值为54
此时的location为1, 值为26
是否需要修改最大值的位置-->No 

此时的location为2, 值为33
是否需要修改最大值的位置-->No 

此时的location为3, 值为24
是否需要修改最大值的位置-->No 

此时的location为4, 值为19
是否需要修改最大值的位置-->No 

此时的location为5, 值为60
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的0
修改之后，最大值的位置为5, 值为60

此时，比较完毕
将最大值60放在5
修改之后的list为 [54, 26, 33, 24, 19, 60, 70]

第3次遍历
此时插入的位置为 4
先假设最大值位于0, 值为54
此时的location为1, 值为26
是否需要修改最大值的位置-->No 

此时的location为2, 值为33
是否需要修改最大值的位置-->No 

此时的location为3, 值为24
是否需要修改最大值的位置-->No 

此时的location为4, 值为19
是否需要修改最大值的位置-->No 

此时，比较完毕
将最大值54放在4
修改之后的list为 [19, 26, 33, 24, 54, 60, 70]

第4次遍历
此时插入的位置为 3
先假设最大值位于0, 值为19
此时的location为1, 值为26
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的0
修改之后，最大值的位置为1, 值为26

此时的location为2, 值为33
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的1
修改之后，最大值的位置为2, 值为33

此时的location为3, 值为24
是否需要修改最大值的位置-->No 

此时，比较完毕
将最大值33放在3
修改之后的list为 [19, 26, 24, 33, 54, 60, 70]

第5次遍历
此时插入的位置为 2
先假设最大值位于0, 值为19
此时的location为1, 值为26
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的0
修改之后，最大值的位置为1, 值为26

此时的location为2, 值为24
是否需要修改最大值的位置-->No 

此时，比较完毕
将最大值26放在2
修改之后的list为 [19, 24, 26, 33, 54, 60, 70]

第6次遍历
此时插入的位置为 1
先假设最大值位于0, 值为19
此时的location为1, 值为24
是否需要修改最大值的位置-->Yes 

此时最大值的位置不是原先的0
修改之后，最大值的位置为1, 值为24

此时，比较完毕
将最大值24放在1
修改之后的list为 [19, 24, 26, 33, 54, 60, 70]

[19, 24, 26, 33, 54, 60, 70]
