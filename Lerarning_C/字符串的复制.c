/*
	字符串的复制
*/

#include <stdio.h>
char* str_copy(char *d, const char *s)
//这个函数的返回值类型是char *，是一个指针
{
	char *t = d;
	//t是起初没有复制的时候，指向被复制的字符串的第一个字符的指针
	while (*d++ = *s++)
	//指针s指向字符串tmp的第一个字符
	//指针d指向字符串str的第一个字符
	//注意这里是=,赋值表达式判断之后的结果是左操作数的类型和值
		;
	return t;
	//最后返回了t，也就是返回了指向复制后的字符串的第一个字符的指针
}
int main(void)
{
	char str[128] = "abc";
	char tmp[128];

	printf("str = \'%s\'\n", str);
	//printf()的时候，可以直接输出指针
	printf("copy:");
	scanf("%s", tmp);
	str_copy(str,   tmp);
	puts("Done!");
	printf("str = \'%s\'\n", str);
	//或者可以这样写
	printf("str = \"%s\"\n", str_copy(str, tmp));

	return 0;
}

str = 'abc'
copy:liyunfei
Done!
str = 'liyunfei'
str = "liyunfei"
