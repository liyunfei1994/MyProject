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
bool is_empty(PNODE pHead);

int length_list(PNODE);
bool insert_list(PNODE, int, int);
bool delete_list(PNODE, int, int *);
void sort_list(PNODE);
bool insert_list(PNODE pHead, int pos, int val);

int main(void)
{

	PNODE pHead = NULL;	//等价于  struct Node * pHead=NULL

	pHead = create_list();	//创建一个非循环单链表，并将该链表的头结点的地址赋给pHead
	traverse_list(pHead);
/*
	if (is_empty(pHead))
		printf("The linked list is empty\n");
	else
		printf("The linked list is not empty\n");
*/
	int len = length_list(pHead);
	printf("The linked list's length is %d\n", len);
	printf("Hello world\n");

	sort_list(pHead);
	traverse_list(pHead);

	printf("insert linked list\n");
	insert_list(pHead, 3, 1994);
	traverse_list(pHead);

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

bool is_empty(PNODE pHead)
{
	if (NULL == pHead->pNext)
		return true;
	else
		return false;
}

int length_list(PNODE pHead)
{
	PNODE p = pHead->pNext;
	int len = 0;

	while (NULL != p)
	{
		++len;
		p = p->pNext;
	}

	return len;
}

void sort_list(PNODE pHead)
{
	int i, j, t;
	int len = length_list(pHead);
	PNODE p, q;

	for (i=0, p=pHead->pNext; i<len-1; ++i, p=p->pNext)
	{
		for (j=i+1, q=p->pNext; j<len; ++j, q=q->pNext)
		{
			if (p->data > q->data)	//类似于数组的: a[i] > a[j]
			{
				t = p->data;	//t = a[i];
				p->data = q->data;	//a[i] = a[j];
				q->data = t;	//a[j] = t;
			}
		}
	}

	return;
}

//在pHead所指向链表的第pos个结点前面插入一个新的结点，该结点的值为val
bool insert_list(PNODE pHead, int pos, int val)
{
	int i=0;
	PNODE p = pHead;

	while (NULL != p && i < pos-1)
	{
		p = p->pNext;
		++i;
	}

	if (i > pos-1 || NULL==p)
		return false;

	PNODE pNew = (PNODE)malloc(sizeof(NODE));
	if (NULL == pNew)
	{
		printf("动态内存分配失败!\n");
		exit(-1);
	}
	pNew->data = val;
	PNODE q = p->pNext;
	p->pNext = pNew;
	pNew->pNext = q;

	return true;
}

----------------
----------------

Please enter the number of list nodes you need to generate: len=3
Please print the value of node 1:90
Please print the value of node 2:20
Please print the value of node 3:8
90 20 8
The linked list's length is 3
Hello world
8 20 90
insert linked list
8 20 1994 90
