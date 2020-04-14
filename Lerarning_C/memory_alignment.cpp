/*
	2020年4月14日21:14:07
	内存对齐
	内存对齐不是C语言的特性，它属于计算机的运行原理，
	C++、Java、Python等其他编程语言同样也会有内存对齐的问题。
*/

#include <stdio.h>
#include <stdlib.h>

struct{
    int a;
    char b;
    int c;
}t={ 10, 'C', 20 };

int m;
char c;
int n;

int main(){

	int o;
	char p;
	int q;

    printf("length: %d\n", sizeof(t));
    printf("Struct\n");
    printf("&a: %X\n&b: %X\n&c: %X\n", &t.a, &t.b, &t.c);
    printf("Global variables\n");
    printf("&m: %X\n&c: %X\n&n: %X\n", &m, &c, &n);
    printf("Local variables\n");
    printf("&o: %X\n&p: %X\n&q: %X\n", &o, &p, &q);
    system("pause");
    return 0;
}

/*
如果不考虑内存对齐，结构体变量 t 所占内存应该为 4+1+4 = 9 个字节。
考虑到内存对齐，虽然成员 b 只占用1个字节，
但它所在的寻址步长内还剩下 3 个字节的空间，放不下一个 int 型的变量了，
所以要把成员 c 放到下一个寻址步长。剩下的这3个字节，作为内存填充浪费掉了
length: 12
Struct
&a: 402000
&b: 402004
&c: 402008
Global variables
对于全局变量，GCC会进行内存对齐
&m: 404008
&c: 40400C
&n: 404010
Local variables
对于局部变量，GCC不会进行内存对齐
&o: 60FF24
&p: 60FF23
&q: 60FF1C
请按任意键继续. . .
*/
