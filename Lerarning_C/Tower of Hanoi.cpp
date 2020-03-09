# include <stdio.h>

/*
	汉诺塔问题，不是线性递归，而是非线性递归
	n = 1--->1
	n = 2--->3
	n = 3--->7
	.....
	汉诺塔的复杂度是2的n次方减1
*/

void hanoi(int n, char A, char B, char C)
{
	/*
	如果是一个盘子
		直接将A柱子上的盘子从A移到C
	否则
		先将A柱子上的n-1个盘子借助C移到B
		再将A柱子上的盘子从A移到C
		最后将B柱子上的n-1个盘子借助A移到C
	*/

	if (1 == n)
	{
		printf("Move the plate %d from %c to %c \n", n, A, C);
	}
	else
	{
		hanoi(n-1, A, C, B);
		printf("Move the plate %d from %c to %c \n", n, A, C);
		hanoi(n-1, B, A, C);
	}
}

int main(void)
{
	char ch1 = 'A';
	char ch2 = 'B';
	char ch3 = 'C';
	int n;

	printf("Please enter the number of plates:");
	scanf("%d", &n);

	hanoi(n, 'A', 'B', 'C');

	return 0;
}

---------------------
---------------------

Please enter the number of plates:3
Move the plate 1 from A to C
Move the plate 2 from A to B
Move the plate 1 from C to B
Move the plate 3 from A to C
Move the plate 1 from B to A
Move the plate 2 from B to C
Move the plate 1 from A to C
