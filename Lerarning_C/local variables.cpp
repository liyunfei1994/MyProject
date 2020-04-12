/*
	2020年4月12日12:24:49
	返回指针的函数的一些问题

	不要使用全局变量在函数之间传递参数和结果
	尽量避免使用全局变量

	使用全局变量和静态本地变量的函数 是多线程不安全的

	最好的做法  是返回传入的指针

	函数的调用，堆栈
*/

#include <stdio.h>

int* f(void);
void g(void);

int main(int argc, char const *argv[])
{
	int *p = f();
	printf("*p = %d\n", *p);  //*p = 12
	g();  //k = 24
	printf("*p = %d\n", *p);  //*p = 24

	return 0;
}

int* f(void)
{
	int i = 12;
	//In f &i = 0060FEF4
	printf("In %s &i = %p\n", __func__, &i);
	// warning: address of local variable `i' returned
	//返回了一个本地变量的地址
	//让外面的程序继续使用它，是有风险的
	//本地变量的地址 会继续分配给别的变量使用
	return &i;
}

void g(void)
{
	int k = 24;
	//In g &k = 0060FEF4
	printf("In %s &k = %p\n", __func__, &k );
	printf("k = %d\n", k);
}
