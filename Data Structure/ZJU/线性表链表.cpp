/*
	2020年3月31日21:49:01
	链表的一些操作
*/

typedef struct LNode * List;
struct LNode
{
	ElementType Data;
	List Next;
};

struct LNode L;
List PtrL;

//求表长
int Length(List PtrL)
{
	//链表遍历
	List p = PtrL; //p指向链表的第一个结点
	int j = 0;
	while (p)
	{
		p = p->Next;
		j++;
	}
	return j;

}
//查找
//1.按序号查找
List FindKth(int K, List PtrL)
{
	List p = PtrL;
	int i = 1;
	while (p != NULL && i < K)
	{
		p = p->Next;
		i++;
	}
	if (i == K)
		return p; //找到第K个，返回指针
	else
		return NULL;
}
//2.按值查找
List Find (ElementType X, List PtrL)
{
	List p = PtrL;
	while (p != NULL && p->Data != X)
	{
		p = p->Next;
	}
	return p;
}
//插入  在第i-1个结点的后面插入一个值为X的结点
//1.先构造一个新的结点，用S指向
//2.再找到链表的第i-1个结点，用p指向
//3.然后修改指针，插入结点
List Insert(ElementType X, int i, List PtrL)
{
	List p, s;
	if (i == 1)
	{
		s = (List)malloc(sizeof(struct LNode));
		s->Data = X;
		s->Next = PtrL;
		return s; //返回新表头的指针
	}
	p = FindKth(i-1, PtrL)
	if (p == NULL)
	{
		printf("参数i错误");
		return NULL;
	}
	else
	{
		s = (List)malloc(sizeof(struct LNode));
		s->Data = X;
		s->Next = p->Next;
		p->Next = s;
		return PtrL;
	}
}
//删除 删除链表的第i个结点
//1.先找到链表的第i-1个结点
//2.再用指针s指向被删除的结点  p的下一个结点
//3.删除s 指向的结点
//4.最后释放s 所指向的结点空间
List Delete(int i, List PtrL)
{
	List p, s;
	if (i == 1)
	{
		s = PtrL;
		if (PtrL != NULL)
			PtrL = PtrL->Next;
		else
			return NULL;
		free(s);
		return PtrL;
	}
	p = FindKth(i-1, PtrL);
	if (p == NULL)
	{
		printf("第%d个结点不存在\n", i-1);
		return NULL;
	}
	else if (p->Next == NULL)
	{
		printf("第%d个结点不存在\n", i);
		return NULL;
	}
	else
	{
		s = p->Next;
		p->Next = s->Next;
		free(s);
		return PtrL;
	}
}
