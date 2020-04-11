/*
	2020年4月11日14:10:45
	union的一个用途
	得到一个整数的内部字节

	union
	所有的成员共享一个空间
	同一时间只有一个成员是有效地
	union的大小是其最大的成员大小
*/


#include <stdio.h>

typedef union {
	int i;
	char ch[sizeof(int)];
} CHI;

int main(int argc, char const *argv[])
{
	CHI chi;
	int i;

	chi.i = 1234; //1234的十六进制是04D2
	for (i = 0; i < sizeof(int); ++i)
	{
		printf("%02hhX", chi.ch[i]);  //输出的结果是D2040000
									//正好和预想的相反，小端 x86
	}
	printf("\n");
	return 0;
}
