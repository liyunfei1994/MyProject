def insertsort(alist):

    for index in range(1, len(alist)):
        print("index = %d" % index)
        print("currentvalue = alist[index]" )
        currentvalue = alist[index]
        print("当前的值currentvalue = %d" % currentvalue)
        print("position = index")
        position = index
        print("此时position为%d" % position)
        print("是否position > 0 并且 alist[position - 1]"
              " %d > currentvalue %d-->%s" %
              (alist[position-1],currentvalue,"Yes" if (position>0 and
                         alist[position-1]>currentvalue) else "No"))
        while position>0 and alist[position-1]>currentvalue:
            print("将position-1的值赋给position")
            alist[position] = alist[position-1]
            print("此时alist为", alist)
            print("修改之后 alist[position]=%d" % alist[position])
            print("position-1 = %d" % (position-1))
            position -= 1
            print("此时position=%d" % position)
            print("判断 position>0并且alist[position-1] %d>currentvalue %d-->%s" %
                  (alist[position-1],currentvalue,"Yes" if (position>0 and alist[position-1]>currentvalue)
                   else "No"))
            print()
        print("将currentvalue %d赋给position %d" % (currentvalue, position))
        alist[position] = currentvalue
        print(alist)
        print()



bbb = [54, 25, 37, 19, 20, 60, 59, 77]
print(bbb)
insertsort(bbb)
print(bbb)


[54, 25, 37, 19, 20, 60, 59, 77]
index = 1
currentvalue = alist[index]
当前的值currentvalue = 25
position = index
此时position为1
是否position > 0 并且 alist[position - 1] 54 > currentvalue 25-->Yes
将position-1的值赋给position
此时alist为 [54, 54, 37, 19, 20, 60, 59, 77]
修改之后 alist[position]=54
position-1 = 0
此时position=0
判断 position>0并且alist[position-1] 77>currentvalue 25-->No

将currentvalue 25赋给position 0
[25, 54, 37, 19, 20, 60, 59, 77]

index = 2
currentvalue = alist[index]
当前的值currentvalue = 37
position = index
此时position为2
是否position > 0 并且 alist[position - 1] 54 > currentvalue 37-->Yes
将position-1的值赋给position
此时alist为 [25, 54, 54, 19, 20, 60, 59, 77]
修改之后 alist[position]=54
position-1 = 1
此时position=1
判断 position>0并且alist[position-1] 25>currentvalue 37-->No

将currentvalue 37赋给position 1
[25, 37, 54, 19, 20, 60, 59, 77]

index = 3
currentvalue = alist[index]
当前的值currentvalue = 19
position = index
此时position为3
是否position > 0 并且 alist[position - 1] 54 > currentvalue 19-->Yes
将position-1的值赋给position
此时alist为 [25, 37, 54, 54, 20, 60, 59, 77]
修改之后 alist[position]=54
position-1 = 2
此时position=2
判断 position>0并且alist[position-1] 37>currentvalue 19-->Yes

将position-1的值赋给position
此时alist为 [25, 37, 37, 54, 20, 60, 59, 77]
修改之后 alist[position]=37
position-1 = 1
此时position=1
判断 position>0并且alist[position-1] 25>currentvalue 19-->Yes

将position-1的值赋给position
此时alist为 [25, 25, 37, 54, 20, 60, 59, 77]
修改之后 alist[position]=25
position-1 = 0
此时position=0
判断 position>0并且alist[position-1] 77>currentvalue 19-->No

将currentvalue 19赋给position 0
[19, 25, 37, 54, 20, 60, 59, 77]

index = 4
currentvalue = alist[index]
当前的值currentvalue = 20
position = index
此时position为4
是否position > 0 并且 alist[position - 1] 54 > currentvalue 20-->Yes
将position-1的值赋给position
此时alist为 [19, 25, 37, 54, 54, 60, 59, 77]
修改之后 alist[position]=54
position-1 = 3
此时position=3
判断 position>0并且alist[position-1] 37>currentvalue 20-->Yes

将position-1的值赋给position
此时alist为 [19, 25, 37, 37, 54, 60, 59, 77]
修改之后 alist[position]=37
position-1 = 2
此时position=2
判断 position>0并且alist[position-1] 25>currentvalue 20-->Yes

将position-1的值赋给position
此时alist为 [19, 25, 25, 37, 54, 60, 59, 77]
修改之后 alist[position]=25
position-1 = 1
此时position=1
判断 position>0并且alist[position-1] 19>currentvalue 20-->No

将currentvalue 20赋给position 1
[19, 20, 25, 37, 54, 60, 59, 77]

index = 5
currentvalue = alist[index]
当前的值currentvalue = 60
position = index
此时position为5
是否position > 0 并且 alist[position - 1] 54 > currentvalue 60-->No
将currentvalue 60赋给position 5
[19, 20, 25, 37, 54, 60, 59, 77]

index = 6
currentvalue = alist[index]
当前的值currentvalue = 59
position = index
此时position为6
是否position > 0 并且 alist[position - 1] 60 > currentvalue 59-->Yes
将position-1的值赋给position
此时alist为 [19, 20, 25, 37, 54, 60, 60, 77]
修改之后 alist[position]=60
position-1 = 5
此时position=5
判断 position>0并且alist[position-1] 54>currentvalue 59-->No

将currentvalue 59赋给position 5
[19, 20, 25, 37, 54, 59, 60, 77]

index = 7
currentvalue = alist[index]
当前的值currentvalue = 77
position = index
此时position为7
是否position > 0 并且 alist[position - 1] 60 > currentvalue 77-->No
将currentvalue 77赋给position 7
[19, 20, 25, 37, 54, 59, 60, 77]

[19, 20, 25, 37, 54, 59, 60, 77]
