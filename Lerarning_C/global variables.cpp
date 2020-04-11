/*
	2020年4月11日21:42:14
	全局变量
*/

#include <stdio.h>

int f(void);

int gAll; //没有做初始化的全局变量会得到0，指针会得到NULL

int main(int argc, char const *argv[])
{
	printf("In %s gAll = %d\n", __func__, gAll);
	f();
	printf("Again In %s gAll = %d\n", __func__, gAll);
	return 0;
}

int f(void)
{	
	//如果函数内部存在与全局变量同名的变量
	//则 全局变量会被隐藏
	int gAll = 1;
	printf("In %s gAll = %d\n", __func__, gAll);
	gAll += 2;
	printf("Again In %s gAll = %d\n", __func__, gAll);
	return gAll;
}
