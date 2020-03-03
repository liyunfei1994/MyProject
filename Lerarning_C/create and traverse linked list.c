# include <stdio.h>
# include <stdlib.h>
# include <malloc.h>

typedef struct Node
{
	int data;	//数据域
	struct Node * pNext;	//指针域
}NODE, *PNODE;	//Node 等价于 struct Node, *PODE 等价于 struct Node *

void traverse_list(PNODE pHead);
PNODE create_list(void);

int main(void)
{

	PNODE pHead = NULL;	//等价于  struct Node * pHead=NULL

	pHead = create_list();	//创建一个非循环单链表，并将该链表的头结点的地址赋给pHead
	traverse_list(pHead);

	printf("Hello world\n");

	return 0;
}

PNODE create_list(void)
{
	int len;	//用来存放有效结点的个数
	int val;	//用来临时存放用户输入的结点的值
	int i;
	//分配了一个不存放有效数据的头结点
	PNODE pHead = (PNODE)malloc(sizeof(NODE));
	if (NULL == pHead)
	{
		printf("分配失败，程序终止！\n");
		exit(-1);
	}

	PNODE pTail = pHead;	
	pTail->pNext = NULL;

	printf("Please enter the number of list nodes you need to generate: len=");
	scanf("%d", &len);

	for (i=0; i<len; ++i)
	{
		printf("Please print the value of node %d:", i+1);
		scanf("%d", &val);

		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		if (NULL == pNew)
		{
			printf("分配失败，程序终止！\n");
			exit(-1);
		}
		//"要把新生成的结点，放在尾结点后面"
		pNew->data = val;
		pTail->pNext = pNew;
		pNew->pNext = NULL;
		pTail = pNew;
	}

	return pHead;

}

void traverse_list(PNODE pHead)
{
	PNODE p = pHead->pNext;	//p指向了首节点

	while (NULL != p)
	{
		printf("%d ", p->data);
		p = p->pNext;
	}
	printf("\n");
	return;
}

------------------
------------------
Please enter the number of list nodes you need to generate: len=4
Please print the value of node 1:19
Please print the value of node 2:20
Please print the value of node 3:0
Please print the value of node 4:-99
19 20 0 -99
Hello world
