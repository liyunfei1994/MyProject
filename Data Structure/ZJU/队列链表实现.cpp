/*
	2020年4月2日14:17:41
	队列的链式存储
	队列的链式存储结构也可以用一个单链表实现
	插入和删除操作分别在链表的两头进行
	front是要做删除操作
	rear是要做插入操作

	链表头 是 front
	链表尾 是 rear
*/

struct Node
{
	ElementType Data;
	struct Node * Next;
};

struct QNode //链队列结构
{
	struct Node * rear; //指向队尾结点
	struct Node * front; //指向对头结点
};

typedef struct QNode * Queue;
Queue PtrQ;

//不带头结点的链式队列出队操作
ElementType DeleteQ(Queue PtrQ)
{
	struct Node * FrontCell;
	ElementType FrontElem;

	if (PtrQ->front == NULL)
	{
		printf("队列空\n");
		return ERROR;
	}
	FrontCell = PtrQ->front;
	if (PtrQ->front == PtrQ->rear)  //若队列只有一个元素
	{
		PtrQ->front=PtrQ->rear = NULL;  //删除后 队列置为空
	}
	else
	{
		PtrQ->front = PtrQ->front->Next;
	}
	FrontElem = FrontCell->Data;
	free(FrontCell);
	return FrontElem;
}
