/*
	2020年4月2日10:23:30
	队列的顺序存储结构
	通常由一个一维数组和一个记录队列头元素位置的变量front
	以及一个记录队列尾元素位置的变量rear组成

*/

#define MaxSize 
struct QNode
{
	ElementType Data[MaxSize];
	int rear;
	int front;
};
typedef struct QNode * Queue;

//循环队列
//堆栈空和满的判别条件是什么
//为什么会出现空、满无法区分的问题？
/*
	1. 使用额外标记
	2. 仅使用n-1个数组空间
	如果全部使用，队列满和空无法判别
*/
//1. 入队
void AddQ(Queue PtrQ, ElementType item)
{
	if(PtrQ->rear+1)%MaxSize == PtrQ->front
	{
		printf("队列满");
		return;
	}
	PtrQ->rear = (PtrQ->rear+1)%MaxSize;
	PtrQ->Data[PtrQ->rear] = item;
}
//2. 出队
ElementType DeleteQ(Queue PtrQ)
{
	if (PtrQ->front == PtrQ->rear)
	{
		printf("队列空");
		return ERROR;
	}
	else
	{
		PtrQ->front = (PtrQ->front+1)%MaxSize;
		return PtrQ->Data[PtrQ->front];
	}
}
