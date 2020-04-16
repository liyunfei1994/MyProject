/*
	2020年4月16日11:32:48
	gets() 函数的使用
	输入字符串
	按下回车才算完
*/

#include <stdio.h>
int main()
{
    char author[30], lang[30], url[30];
    gets(author);
    printf("author: %s\n", author);
    gets(lang);
    printf("lang: %s\n", lang);
    gets(url);
    printf("url: %s\n", url);
   
    return 0;
}
/*
liyunfei wenchuanyi
author: liyunfei wenchuanyi
hahaha * hhhh
lang: hahaha * hhhh
:::: 92393eq
url: :::: 92393eq
*/
/*gets() 是有缓冲区的，每次按下回车键，就代表当前输入结束了，gets() 开始从缓冲区中读取内容，这一点和 scanf() 是一样的。gets() 和 scanf() 的主要区别是：
scanf() 读取字符串时以空格为分隔，遇到空格就认为当前字符串结束了，所以无法读取含有空格的字符串。
gets() 认为空格也是字符串的一部分，只有遇到回车键时才认为字符串输入结束，所以，不管输入了多少个空格，只要不按下回车键，对 gets() 来说就是一个完整的字符串。

也就是说，gets() 能读取含有空格的字符串，而 scanf() 不能。
*/
