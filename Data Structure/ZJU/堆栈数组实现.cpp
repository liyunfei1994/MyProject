/*
	2020年4月1日17:56:16
	栈的顺序存储结构 用数组实现
	通常由一个一维数组和一个记录栈顶元素位置的变量组成
*/

#define MaxSize //储存数据元素的最大个数
typedef struct SNode * Stack;
struct SNode
{
	ElementType Data[MaxSize];
	int Top;  //栈顶元素的数组下标
};

//1.入栈
void Push(Stack PtrS, ElementType item)
{
	if (PtrS->Top == MaxSize-1)
	{
		printf("堆栈满");
		return;
	}
	else
	{
		//形象的理解可以是i++先做别的事，再自己加1，
		//++i先自己加1，再做别的事情。
		PtrS->Data[++(PtrS->Top)] = item;
		return;
	}
}
//出栈
ElementType Pop(Stack PtrS)
{
	if (PtrS->Top == -1)
	{
		printf("堆栈空");
		return ERROR; //ERROR是ElementType的特殊标记值
	}
	else
	{
		return (PtrS->Data[(PtrS->Top)--]);
	}
}
//请用一个数组实现两个堆栈，要求最大化的利用数组空间
//要求数组只要有空间，入栈操作就能成功
//一种方法是  使这两个栈分别从数组的两头开始想中间生长
//当两个栈的栈顶指针相遇时，表示两个栈都满了
#define MaxSize
struct DStack
{
	ElementType Data[MaxSize];
	int Top1;
	int Top2;
} S;
//这两个标志，表示这两个栈都是空的
S.Top1 = -1;
S.Top2 = MaxSize;

void Push(struct DStack * PtrS, ElementType item, int Tag)
{
	/* Tag 作为区分两个堆栈的标志，取值为1和2 */
	if (PtrS->Top2 - PtrS->Top1 == 1)
	{
		printf("堆栈满");
		return;
	}
	if (Tag == 1) /* 对第一个堆栈操作 */
	{
		PtrS->Data[++(PtrS->Top1)] = item;
	}
	else /* 对第二个堆栈操作 */
	{
		PtrS->Data[--(PtrS->Top2)] = item;
	}
}

ElementType Pop(struct DStack * PtrS, int Tag)
{
	if (Tag == 1) //对第一个堆栈操作
	{
		if (PtrS ->Top1 == -1) //堆栈1 为空
		{
			printf("堆栈1空");
			return NULL;
		}
		else
			return PtrS->Data[(PtrS->Top1)--];
	}
	else	//对第二个堆栈操作
	{
		if (PtrS->Top2 == MaxSize)
		{
			printf("堆栈2空");
			return NULL;
		}
		else
			return PtrS->Data[(PtrS->Top2)++];
	}
}
