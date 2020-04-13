#include <stdio.h>

int main(int argc, char const *argv[])
{
	int arr[] = {99, 15, 100, 200, 88};

	int i;
	int *p = arr;
	int len = sizeof(arr)/sizeof(int);

	for (i = 0; i < len; ++i)
	{
		printf("%d = %d\n", i, *p++);
	}

	/*
		假设p 是指向数组arr中第n个元素的指针
		*p++ 等价于*(p++)
		表示先取得第n个元素的值
		再将p指向下一个元素
	*/
	return 0;
}

-------------
0 = 99
1 = 15
2 = 100
3 = 200
4 = 88
