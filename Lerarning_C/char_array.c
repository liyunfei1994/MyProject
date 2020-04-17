/*
	2020年4月16日21:42:11
	字符串的两种表示方式

	C语言中没有特定的字符串类型，我们通常是将字符串放在一个字符数组中
*/

#include <stdio.h>
#include <string.h>
int main(){
    char str[] = "http://c.biancheng.net";
    int len = strlen(str), i;
    //直接输出字符串
    printf("%s\n", str);
    //每次输出一个字符
    for(i=0; i<len; i++){
        printf("%c", str[i]);
    }
    printf("\n");
    return 0;
}

#include <stdio.h>
#include <string.h>
int main(){
    char str[] = "http://c.biancheng.net";
    char *pstr = str;
    int len = strlen(str), i;
    //使用*(pstr+i)
    for(i=0; i<len; i++){
        printf("%c", *(pstr+i));
    }
    printf("\n");
    //使用pstr[i]
    for(i=0; i<len; i++){
        printf("%c", pstr[i]);
    }
    printf("\n");
    //使用*(str+i)
    for(i=0; i<len; i++){
        printf("%c", *(str+i));
    }
    printf("\n");
    return 0;
}

//除了字符数组之外，C 语言还支持另外一种表示字符串的方法
//就是使用一个指针指向字符串
char *str = "http://c.biancheng.net";

#include <stdio.h>
#include <string.h>
int main(){
    char *str = "http://c.biancheng.net";
    int len = strlen(str), i;
   
    //直接输出字符串
    printf("%s\n", str);
    //使用*(str+i)
    for(i=0; i<len; i++){
        printf("%c", *(str+i));
    }
    printf("\n");
    //使用str[i]
    for(i=0; i<len; i++){
        printf("%c", str[i]);
    }
    printf("\n");
    return 0;
}

//那这两种表示字符串的方式有没有区别呢？
/*
有！它们最根本的区别是在内存中的存储区域不一样，
字符数组存储在全局数据区或栈区，
第二种形式的字符串存储在常量区。
全局数据区和栈区的字符串（也包括其他数据）有读取和写入的权限，
而常量区的字符串（也包括其他数据）只有读取权限，没有写入权限。

内存权限的不同导致的一个明显结果就是，
字符数组在定义后可以读取和修改每个字符，
而对于第二种形式的字符串，一旦被定义后就只能读取不能修改，
任何对它的赋值都是错误的。

我们将第二种形式的字符串称为  字符串常量，
意思很明显，常量只能读取不能写入
*/

#include <stdio.h>
int main(){
    char *str = "Hello World!";
    str = "I love C!";  //正确
    str[3] = 'P';  //错误
    return 0;
}

/*
第4行代码是正确的，
可以更改指针变量本身的指向；
第5行代码是错误的，不能修改字符串中的字符。
*/

/*
获取用户输入的字符串就是一个典型的写入操作，
只能使用字符数组，不能使用字符串常量，
*/

#include <stdio.h>
int main(){
    char str[30];
    gets(str);
    printf("%s\n", str);
    return 0;
}

/*
最后我们来总结一下，C语言有两种表示字符串的方法，
一种是字符数组，另一种是字符串常量，
它们在内存中的存储位置不同，
使得字符数组可以读取和修改，
而字符串常量只能读取不能修改。
*/
