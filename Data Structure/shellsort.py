def shellsort(alist):
    count =1
    gap = len(alist) // 2
    print("gap=", gap)
    print("判断gap是否大于0-->%s" % ("Yes" if gap > 0 else "No"))
    while gap > 0:
        print("第%d次遍历" % count)
        print("此时gap=", gap)
        for startposition in range(gap):
            print("开始startposition的遍历")
            print("startposition=", startposition)
            gapinsertsort(alist, startposition, gap)

        print("After increments of size", gap, "The list is", alist)
        print()
        count += 1
        gap //= 2
        print("判断gap是否大于0-->%s" % ("Yes" if gap > 0 else "No"))


def gapinsertsort(alist, start, gap):
    print()
    print("此时进入gapinsert 函数")
    count = 1
    for i in range(start+gap, len(alist), gap):
        print("第%d次range小遍历" % count)
        print("start+gap=", start+gap, "列表长度为", len(alist), "gap=", gap)
        print("i=", i)
        currentvalue = alist[i]
        print("currentvalue=alist[%d]=%d" % (i, currentvalue))
        position = i
        print("position=", position)
        print("判断是否position %d>=gap %d and alist[position-gap=%d] %d >currentvalue %d-->%s" % (
            position, gap, position-gap,alist[position-gap], currentvalue,
            "Yes" if (position >= gap and alist[position-gap] > currentvalue) else "No"
        ))
        while position >= gap and alist[position-gap] > currentvalue:
            print("将position-gap %d的值%d赋给position %d" % (position-gap,alist[position-gap], position))
            alist[position] = alist[position-gap]
            print("alist[position %d]=%d" % (position, alist[position]))
            position -= gap
            print("将position-gap,此时position=%d" % position)
            print("判断是否position %d>=gap %d and alist[position-gap=%d] %d >currentvalue %d-->%s" % (
                position, gap, position-gap ,alist[position - gap],currentvalue,
                "Yes" if (position >= gap and alist[position - gap] > currentvalue) else "No"
            ))
        print("alist[position %d]=currentvalue %d" % (position, currentvalue))
        alist[position] = currentvalue
        # print("此时交换了position-gap %d的值和position %d的值" % (position-gap, position))
        print("alist=",alist)
        count += 1
        print()


bbb = [54, 26, 77, 93, 17, 44, 55, 20]
shellsort(bbb)
print(bbb)


gap= 4
判断gap是否大于0-->Yes
第1次遍历
此时gap= 4
开始startposition的遍历
startposition= 0

此时进入gapinsert 函数
第1次range小遍历
start+gap= 4 列表长度为 8 gap= 4
i= 4
currentvalue=alist[4]=17
position= 4
判断是否position 4>=gap 4 and alist[position-gap=0] 54 >currentvalue 17-->Yes
将position-gap 0的值54赋给position 4
alist[position 4]=54
将position-gap,此时position=0
判断是否position 0>=gap 4 and alist[position-gap=-4] 54 >currentvalue 17-->No
alist[position 0]=currentvalue 17
alist= [17, 26, 77, 93, 54, 44, 55, 20]

开始startposition的遍历
startposition= 1

此时进入gapinsert 函数
第1次range小遍历
start+gap= 5 列表长度为 8 gap= 4
i= 5
currentvalue=alist[5]=44
position= 5
判断是否position 5>=gap 4 and alist[position-gap=1] 26 >currentvalue 44-->No
alist[position 5]=currentvalue 44
alist= [17, 26, 77, 93, 54, 44, 55, 20]

开始startposition的遍历
startposition= 2

此时进入gapinsert 函数
第1次range小遍历
start+gap= 6 列表长度为 8 gap= 4
i= 6
currentvalue=alist[6]=55
position= 6
判断是否position 6>=gap 4 and alist[position-gap=2] 77 >currentvalue 55-->Yes
将position-gap 2的值77赋给position 6
alist[position 6]=77
将position-gap,此时position=2
判断是否position 2>=gap 4 and alist[position-gap=-2] 77 >currentvalue 55-->No
alist[position 2]=currentvalue 55
alist= [17, 26, 55, 93, 54, 44, 77, 20]

开始startposition的遍历
startposition= 3

此时进入gapinsert 函数
第1次range小遍历
start+gap= 7 列表长度为 8 gap= 4
i= 7
currentvalue=alist[7]=20
position= 7
判断是否position 7>=gap 4 and alist[position-gap=3] 93 >currentvalue 20-->Yes
将position-gap 3的值93赋给position 7
alist[position 7]=93
将position-gap,此时position=3
判断是否position 3>=gap 4 and alist[position-gap=-1] 93 >currentvalue 20-->No
alist[position 3]=currentvalue 20
alist= [17, 26, 55, 20, 54, 44, 77, 93]

After increments of size 4 The list is [17, 26, 55, 20, 54, 44, 77, 93]

判断gap是否大于0-->Yes
第2次遍历
此时gap= 2
开始startposition的遍历
startposition= 0

此时进入gapinsert 函数
第1次range小遍历
start+gap= 2 列表长度为 8 gap= 2
i= 2
currentvalue=alist[2]=55
position= 2
判断是否position 2>=gap 2 and alist[position-gap=0] 17 >currentvalue 55-->No
alist[position 2]=currentvalue 55
alist= [17, 26, 55, 20, 54, 44, 77, 93]

第2次range小遍历
start+gap= 2 列表长度为 8 gap= 2
i= 4
currentvalue=alist[4]=54
position= 4
判断是否position 4>=gap 2 and alist[position-gap=2] 55 >currentvalue 54-->Yes
将position-gap 2的值55赋给position 4
alist[position 4]=55
将position-gap,此时position=2
判断是否position 2>=gap 2 and alist[position-gap=0] 17 >currentvalue 54-->No
alist[position 2]=currentvalue 54
alist= [17, 26, 54, 20, 55, 44, 77, 93]

第3次range小遍历
start+gap= 2 列表长度为 8 gap= 2
i= 6
currentvalue=alist[6]=77
position= 6
判断是否position 6>=gap 2 and alist[position-gap=4] 55 >currentvalue 77-->No
alist[position 6]=currentvalue 77
alist= [17, 26, 54, 20, 55, 44, 77, 93]

开始startposition的遍历
startposition= 1

此时进入gapinsert 函数
第1次range小遍历
start+gap= 3 列表长度为 8 gap= 2
i= 3
currentvalue=alist[3]=20
position= 3
判断是否position 3>=gap 2 and alist[position-gap=1] 26 >currentvalue 20-->Yes
将position-gap 1的值26赋给position 3
alist[position 3]=26
将position-gap,此时position=1
判断是否position 1>=gap 2 and alist[position-gap=-1] 93 >currentvalue 20-->No
alist[position 1]=currentvalue 20
alist= [17, 20, 54, 26, 55, 44, 77, 93]

第2次range小遍历
start+gap= 3 列表长度为 8 gap= 2
i= 5
currentvalue=alist[5]=44
position= 5
判断是否position 5>=gap 2 and alist[position-gap=3] 26 >currentvalue 44-->No
alist[position 5]=currentvalue 44
alist= [17, 20, 54, 26, 55, 44, 77, 93]

第3次range小遍历
start+gap= 3 列表长度为 8 gap= 2
i= 7
currentvalue=alist[7]=93
position= 7
判断是否position 7>=gap 2 and alist[position-gap=5] 44 >currentvalue 93-->No
alist[position 7]=currentvalue 93
alist= [17, 20, 54, 26, 55, 44, 77, 93]

After increments of size 2 The list is [17, 20, 54, 26, 55, 44, 77, 93]

判断gap是否大于0-->Yes
第3次遍历
此时gap= 1
开始startposition的遍历
startposition= 0

此时进入gapinsert 函数
第1次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 1
currentvalue=alist[1]=20
position= 1
判断是否position 1>=gap 1 and alist[position-gap=0] 17 >currentvalue 20-->No
alist[position 1]=currentvalue 20
alist= [17, 20, 54, 26, 55, 44, 77, 93]

第2次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 2
currentvalue=alist[2]=54
position= 2
判断是否position 2>=gap 1 and alist[position-gap=1] 20 >currentvalue 54-->No
alist[position 2]=currentvalue 54
alist= [17, 20, 54, 26, 55, 44, 77, 93]

第3次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 3
currentvalue=alist[3]=26
position= 3
判断是否position 3>=gap 1 and alist[position-gap=2] 54 >currentvalue 26-->Yes
将position-gap 2的值54赋给position 3
alist[position 3]=54
将position-gap,此时position=2
判断是否position 2>=gap 1 and alist[position-gap=1] 20 >currentvalue 26-->No
alist[position 2]=currentvalue 26
alist= [17, 20, 26, 54, 55, 44, 77, 93]

第4次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 4
currentvalue=alist[4]=55
position= 4
判断是否position 4>=gap 1 and alist[position-gap=3] 54 >currentvalue 55-->No
alist[position 4]=currentvalue 55
alist= [17, 20, 26, 54, 55, 44, 77, 93]

第5次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 5
currentvalue=alist[5]=44
position= 5
判断是否position 5>=gap 1 and alist[position-gap=4] 55 >currentvalue 44-->Yes
将position-gap 4的值55赋给position 5
alist[position 5]=55
将position-gap,此时position=4
判断是否position 4>=gap 1 and alist[position-gap=3] 54 >currentvalue 44-->Yes
将position-gap 3的值54赋给position 4
alist[position 4]=54
将position-gap,此时position=3
判断是否position 3>=gap 1 and alist[position-gap=2] 26 >currentvalue 44-->No
alist[position 3]=currentvalue 44
alist= [17, 20, 26, 44, 54, 55, 77, 93]

第6次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 6
currentvalue=alist[6]=77
position= 6
判断是否position 6>=gap 1 and alist[position-gap=5] 55 >currentvalue 77-->No
alist[position 6]=currentvalue 77
alist= [17, 20, 26, 44, 54, 55, 77, 93]

第7次range小遍历
start+gap= 1 列表长度为 8 gap= 1
i= 7
currentvalue=alist[7]=93
position= 7
判断是否position 7>=gap 1 and alist[position-gap=6] 77 >currentvalue 93-->No
alist[position 7]=currentvalue 93
alist= [17, 20, 26, 44, 54, 55, 77, 93]

After increments of size 1 The list is [17, 20, 26, 44, 54, 55, 77, 93]

判断gap是否大于0-->No
[17, 20, 26, 44, 54, 55, 77, 93]
