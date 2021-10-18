/*
C 库函数 void *memset(void *str, int c, size_t n) 
复制字符 c（一个无符号字符）到参数 str 所指向的字符串的前 n 个字符。
*/

#include <stdio.h>
#include <string.h>
 
int main ()
{
   char str[50];
 
   strcpy(str,"This is string.h library function");
   puts(str);
 
   memset(str,'$',7);
   puts(str);
   
   return(0);
}

----------------------
This is string.h library function
$$$$$$$ string.h library function
