/*
    2020年6月3日12:06:38
    链表的一些基本操作
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Link {
    int  elem;
    struct Link *next;
}link;

link * initLink();
//链表插入的函数，p是链表，elem是插入的结点的数据域，add是插入的位置
link * insertElem(link * p, int elem, int add);
//删除结点的函数，p代表操作链表，add代表删除节点的位置
link * delElem(link * p, int add);
//查找结点的函数，elem为目标结点的数据域的值
int selectElem(link * p, int elem);
//更新结点的函数，newElem为新的数据域的值
link *amendElem(link * p, int add, int newElem);

void display(link *p);

int main() {
    //初始化链表（1，2，3，4）
    printf("Initialize Linked list:\n");
    link *p = initLink();
    display(p);

    printf("Insert element 5 at position 4\n");
    p = insertElem(p, 5, 4);
    display(p);

    printf("Delete element 3:\n");
    p = delElem(p, 3);
    display(p);

    printf("Find the position of element 2\n");
    int address = selectElem(p, 2);
    if (address == -1) {
        printf("without the element");
    }
    else {
        printf("The position of element 2 is: %d\n", address);
    }
    printf("Modify the element at the position 3 to 7:\n");
    p = amendElem(p, 3, 7);
    display(p);

    return 0;
}

link * initLink() {
    link * p = (link*)malloc(sizeof(link));//创建一个头结点
    link * temp = p;//声明一个指针指向头结点，用于遍历链表
    //生成链表
    for (int i = 1; i < 5; i++) {
        link *a = (link*)malloc(sizeof(link));
        a->elem = i;
        a->next = NULL;
        temp->next = a;
        temp = temp->next;
    }
    return p;
}

link * insertElem(link * p, int elem, int add) {
    link * temp = p;//创建临时结点temp
    //首先找到要插入位置的上一个结点
    for (int i = 1; i < add; i++) {
        temp = temp->next;
        if (temp == NULL) {
            printf("插入位置无效\n");
            return p;
        }
    }
    //创建插入结点c
    link * c = (link*)malloc(sizeof(link));
    c->elem = elem;
    //向链表中插入结点
    c->next = temp->next;
    temp->next = c;
    return  p;
}

link * delElem(link * p, int add) {
    link * temp = p;
    //遍历到被删除结点的上一个结点
    for (int i = 1; i < add; i++) {
        temp = temp->next;
        if (temp->next == NULL) {
            printf("没有该结点\n");
            return p;
        }
    }
    link * del = temp->next;//单独设置一个指针指向被删除结点，以防丢失
    temp->next = temp->next->next;//删除某个结点的方法就是更改前一个结点的指针域
    free(del);//手动释放该结点，防止内存泄漏
    return p;
}

int selectElem(link * p, int elem) {
    link * t = p;
    int i = 1;
    while (t->next) {
        t = t->next;
        if (t->elem == elem) {
            return i;
        }
        i++;
    }
    return -1;
}
link *amendElem(link * p, int add, int newElem) {
    link * temp = p;
    temp = temp->next;//tamp指向首元结点
    //temp指向被删除结点
    for (int i = 1; i < add; i++) {
        temp = temp->next;
    }
    temp->elem = newElem;
    return p;
}
void display(link *p) {
    link* temp = p;//将temp指针重新指向头结点
    //只要temp指针指向的结点的next不是Null，就执行输出语句。
    while (temp->next) {
        temp = temp->next;
        printf("%d ", temp->elem);
    }
    printf("\n");
}

/*
Initialize Linked list:
1 2 3 4
Insert element 5 at position 4
1 2 3 5 4
Delete element 3:
1 2 5 4
Find the position of element 2
The position of element 2 is: 2
Modify the element at the position 3 to 7:
1 2 7 4
*/
