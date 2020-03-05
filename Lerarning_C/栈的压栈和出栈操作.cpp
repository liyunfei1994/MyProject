# include <stdio.h>
# include <malloc.h>
# include <stdlib.h>

typedef struct Node
{
	int data;
	struct Node * pNext;
}NODE,* PNODE;

typedef struct stack
{
	PNODE pTop;
	PNODE pBottom;
}STACK, * PSTACK;

void init(PSTACK);
void push(PSTACK, int);
void traverse(PSTACK);
bool pop(PSTACK, int *);

int main(void)
{
	STACK S;
	int val;

	init(&S);	//目的是造出一个空栈
	push(&S, 1);	//压栈
	push(&S, 2);
	push(&S, 10);
	push(&S, 9);
	printf("The stack contain:");
	traverse(&S);	//遍历

	if (pop(&S, &val))
	{
		printf("pop complete! pop value is %d\n", val);
	}
	else
	{
		printf("pop fail!\n");
	}
	printf("After pop, the stack contain:");
	traverse(&S);

	return 0;
}

void init(PSTACK pS)
{
	pS->pTop = (PNODE)malloc(sizeof(NODE));
	if (NULL == pS->pTop)
	{
		printf("动态内存分配失败!\n");
		exit(-1);
	}
	else
	{
		pS->pBottom = pS->pTop;
		pS->pTop->pNext = NULL;
	}
}

void push(PSTACK pS, int val)
{
	PNODE pNew = (PNODE)malloc(sizeof(NODE));
	pNew->data = val;
	pNew->pNext = pS->pTop;
	pS->pTop = pNew;

	return;
}

void traverse(PSTACK pS)
{
	PNODE p = pS->pTop;

	while (p != pS->pBottom)
	{
		printf("%d ",p->data);
		p = p->pNext;
	}
	printf("\n");

	return;
}

bool empty(PSTACK pS)
{
	if (pS->pBottom == pS->pTop)
		return true;
	else
		return false;
}

bool pop(PSTACK pS, int * pVal)
{
	if (empty(pS))
	{
		return false;
	}
	else
	{
		PNODE r = pS->pTop;
		* pVal = r->data;
		pS->pTop = r->pNext;
		free(r);
		r = NULL;

		return true;
	}
}

-------------------
-------------------

The stack contain:9 10 2 1
pop complete! pop value is 9
After pop, the stack contain:10 2 1
