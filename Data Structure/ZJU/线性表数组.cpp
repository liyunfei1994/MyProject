/*
	2020年3月31日21:45:43
	线性表 数组的一些操作
	初始化，查找，增加，删除
*/

typedef struct LNode * List;
struct LNode
{
	elementype data[maxsize];
	int last;
};

struct LNode L;
List Ptrl;

/*
访问下标为i的元素，L.data[i] 或者 Ptrl->data[i]
线性表的长度：L.last +1 或者 Ptrl->last+1
*/
//初始化（建立空的顺序表）
List MakeEmpty()
{
	List Ptrl;
	Ptrl = (List)malloc(sizeof(struct LNode));
	Ptrl->last = -1;
	return Ptrl;
}
//查找
int Find(elementype X, List Ptrl)
{
	int i = 0;
	while (i <= Ptrl->last && Ptrl->data[i] != X)
		i++;

	if (i > Ptrl->last)
		return -1;
	else
		return i;
}
//插入 在第i个位置插入X元素
void Insert(elementype X, int i, List Ptrl)
{
	int j;
	if (Ptrl->last == maxsize-1) //表空间已满， 不能插入
	{
		printf("表满\n");
		return;
	}
	if (i < 1 || i > Ptrl->last + 2)
	{
		printf("位置不合法\n");
		return;
	}
	for (j = Ptrl->last; j >= i-1; j--)
	{
		Ptrl->data[j+1] = Ptrl->data[j];
	}
	Ptrl->data[i-1] = X;
	Ptrl->last++;
	return;
}
//删除 删除表的第i个位置上的元素X
void delete(int i, List Ptrl)
{
	int j;
	if (i < 1 || i > Ptrl->last+1)
	{
		printf("不存在第%d个元素", i);
		return;
	}
	for (j = i; j <= Ptrl->last; j++)
	{
		Ptrl->data[j-1] = Ptrl->data[j];
	}
	Ptrl->last--;
	return;

}
