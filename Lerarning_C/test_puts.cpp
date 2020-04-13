/*
	2020年4月13日21:20:53
	字符串的输出
*/
#include <stdio.h>

int main(){
    char str[] = "http://c.biancheng.net";
    printf("%s\n", str);  //通过字符串名字输出
    printf("%s\n", "http://c.biancheng.net");  //直接输出
    puts(str);  //通过字符串名字输出
    puts("http://c.biancheng.net");  //直接输出

    char str1[4] = {0};
    printf("%s\n", str1);
    return 0;
}

/*
	输出字符串时只需要给出名字，不能带后边的[ ]
	例如，下面的两种写法都是错误的：
	printf("%s\n", str[]);
	puts(str[10]);
*/
