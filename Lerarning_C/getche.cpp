/*
	2020年4月16日11:06:39
	getche() 的使用
	注意，getche() 位于 conio.h 头文件中，
	而这个头文件是 Windows 特有的，
	Linux 和 Mac OS 下没有包含该头文件。
	换句话说，getche() 并不是标准函数，默认只能在 Windows 下使用，
	不能在 Linux 和 Mac OS 下使用。
*/

#include <stdio.h>
#include <conio.h>

int main(int argc, char const *argv[])
{
	char c = getche();
	printf("c: %c\n", c);

	return 0;
}

/*
3c: 3
*/
