/*
    2020年4月15日10:55:08
    用户空间的内存分布情况
    程序代码区：存放函数体的二进制代码
    常量区：存放一般的常量、字符串常量
    全局数据区：存放全局变量，静态变量
    堆区：一般由程序员分配和释放，若程序员不释放，程序运行结束时由操作系统回收
    这里的堆区和数据结构的堆不是一个概念
    动态链接库：用于在程序运行期间加载和卸载动态链接库
    栈区：存放函数的参数值，局部变量值，类似于数据结构中的栈

    常量区、全局数据区、栈区的内存有操作系统自动分配和释放，不能由程序员控制

    程序员唯一能控制的就是堆
*/

#include <stdio.h>

char *str1 = "c.biancheng.net";  //字符串在常量区，str1在全局数据区
//全局变量的内存在编译时就已经分配好了，它的默认初始值是 0
int n;  //全局数据区
char* func(){
    char *str = "C Language";  //字符串在常量区，str在栈区
    return str;
}
int main(){
    int a;  //栈区
    char *str2 = "01234";  //字符串在常量区，str2在栈区
    //字符数组 arr[20] 在栈区分配内存，
    //字符串"56789"就保存在这块内存中，而不是在常量区，
    char  arr[20] = "56789";  //字符串和arr都在栈区
    char *pstr = func();  //栈区
    int b;  //栈区
    printf("Constant Area\n");
    printf("str1: %#X\npstr: %#X\nstr2: %#X\n", str1, pstr, str2);
    puts("--------------");
    printf("&str1: %#X\n   &n: %#X\n", &str1, &n);
    puts("--------------");
    printf("  &a: %#X\n arr: %#X\n  &b: %#X\n", &a, arr, &b);
    puts("--------------");
    printf("n: %d\na :%d\nb: %d\n", n, a, b);
    puts("--------------");
    printf("%s\n", pstr);
    return 0;
}

/*
Constant Area
str1: 0X403000
pstr: 0X403010
str2: 0X40301B
--------------
全局数据区
&str1: 0X402000
   &n: 0X404008
--------------
栈区
  &a: 0X60FF1C
 arr: 0X60FEF0
  &b: 0X60FEE8
--------------
n: 0
a :4199590
b: 4199040
--------------
C Language
*/
