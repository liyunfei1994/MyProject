/*
	如果没有指针，没法处理的问题
*/

#include <stdio.h>
void sum_diff(int n1, int n2, int sum, int diff)
{
	sum = n1 + n2;
	printf("In sum_diff:sum=%d \n", sum);

	diff = (n1 > n2)?n1-n2:n2-n1;
	printf("In sum_diff:diff=%d \n", diff);
}
/*
	main 函数调用sum_diff函数的时候，实参na, nb, wa, sa的值
	会分别传给形参n1, n2, sum和diff
	但是，这个传递只是值的传递，而且是单向的传递
	即使在sum_diff函数的内部改变了sum和diff的值，也无法将其带到main函数中
	另外，函数返回到调用源的返回值只能有一个，无法将sum和diff同时返回
*/

int main(void)
{
	int na, nb;
	int wa = 0, sa = 0;
	puts("please enter two numbers.");
	printf("A:");	scanf("%d", &na);
	printf("B:");	scanf("%d", &nb);
	sum_diff(na,nb,wa,sa);
	printf("In main, sum is %d, diff is %d\n", wa, sa);

	return 0;
}
