/*
	2020年4月1日19:41:28
	堆栈的链式存储实现
	栈的链式存储结构实际上就是一个单链表
	**
	链表的尾部是不可以作为栈顶指针Top的
	链表的头部作为栈顶指针！！
	**
*/

typedef struct SNode * Stack;
struct SNode
{
	ElementType Data;
	struct SNode * Next;
};

//1.堆栈初始化
Stack CreateStack()
{
	//构建一个堆栈的头结点，返回指针
	Stack S;
	S = (Stack)malloc(sizeof(struct SNode));
	S->Next = NULL;
	return S;
}
//2.判断堆栈S是否为空
int IsEmpty(Stack S)
{
	return (S->Next == NULL);
}
//3.插入
void Push(ElementType item, Stack S)
{	
	//往堆栈的头上插入结点
	struct SNode * TmpCell;
	TmpCell = (struct SNode *)malloc(sizeof(struct SNode));
	TmpCell->Data = item;
	TmpCell->Next = S->Next;
	S->Next = TmpCell;
}
//4.删除
ElementType Pop(Stack S)
{
	struct SNode * FirstCell;
	ElementType TopElem;
	if (IsEmpty(S))
	{
		printf("堆栈空");
		return NULL;
	}
	else
	{
		FirstCell = S->Next;
		S->Next = FirstCell->Next;
		TopElem = FirstCell->Data;
		free(FirstCell);
		return TopElem;
	}
}
