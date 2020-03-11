# include <stdio.h>
# include <malloc.h>

/*
	链式二叉树，静态构造，没有使用递归
*/

struct BTNode
{
	char data;
	struct BTNode * pLchild;
	struct BTNode * pRchild;
};

struct BTNode * CreateBTree();
void PreTraverseBTree(struct BTNode *);
void InTraverseBTree(struct BTNode *);
void PostTraverseBTree(struct BTNode *);

int main(void)
{
	struct BTNode * pT = CreateBTree();

	printf("Preorder traverse:\n");
	PreTraverseBTree(pT);
	printf("\n");
	printf("Inorder traverse:\n");	//先序遍历-->ABCDE
	InTraverseBTree(pT);	//中序遍历-->BADEC
	printf("\n");
	printf("Postorder traverse:\n");
	PostTraverseBTree(pT);	//后序遍历-->BEDCA

	return 0;
}

void PreTraverseBTree(struct BTNode * pT)
{
	/*
		先访问根节点
		再先序遍历左子树
		再先序遍历右子树
	*/

	if (NULL != pT)
	{	
		printf("%c ", pT->data);
		if (NULL != pT->pLchild)
			PreTraverseBTree(pT->pLchild);
		if (NULL != pT->pRchild)
			PreTraverseBTree(pT->pRchild);
	}
}

void InTraverseBTree(struct BTNode * pT)
{

	if (NULL != pT)
	{	
		
		if (NULL != pT->pLchild)
			InTraverseBTree(pT->pLchild);
		printf("%c ", pT->data);
		if (NULL != pT->pRchild)
			InTraverseBTree(pT->pRchild);
	}
}

void PostTraverseBTree(struct BTNode * pT)
{
	
	if (NULL != pT)
	{	
		
		if (NULL != pT->pLchild)
			PostTraverseBTree(pT->pLchild);
		
		if (NULL != pT->pRchild)
			PostTraverseBTree(pT->pRchild);

		printf("%c ", pT->data);
	}
}

struct BTNode * CreateBTree(void)
{
	struct BTNode * pA = (struct BTNode *)malloc(sizeof(struct BTNode));
	struct BTNode * pB = (struct BTNode *)malloc(sizeof(struct BTNode));
	struct BTNode * pC = (struct BTNode *)malloc(sizeof(struct BTNode));
	struct BTNode * pD = (struct BTNode *)malloc(sizeof(struct BTNode));
	struct BTNode * pE = (struct BTNode *)malloc(sizeof(struct BTNode));

	pA->data = 'A';
	pB->data = 'B';
	pC->data = 'C';
	pD->data = 'D';
	pE->data = 'E';

	pA->pLchild = pB;
	pA->pRchild = pC;
	pB->pLchild = pB->pRchild = NULL;
	pC->pLchild = pD;
	pC->pRchild = NULL;
	pD->pLchild = NULL;
	pD->pRchild = pE;
	pE->pLchild = pE->pRchild = NULL;

	return pA;
}

--------------------
--------------------

Preorder traverse:
A B C D E
Inorder traverse:
B A D E C
Postorder traverse:
B E D C A
