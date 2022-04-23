#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
一、运算顺序不同

1、n++：后执行自增运算。

2、++n：先执行自增运算。

二、内存顺序不同

1、n++：先访问参数n，之后将参数n加1。

2、++n：先将参数n加1，之后再访问参数n。

三、结果不同

1、n++：输出的结果为 n。
2、++n：输出的结果为 n+1。
*/

static bool isValid(char *s)
{
    int n = 0;
    char stack[100];

    while (*s != '\0') {
        switch(*s) {
        case '(':
        case '[':
        case '{':
            stack[n++] = *s;
            break;
        case ')':
            if (n == 0 || stack[--n] != '(') return false;
            break;
        case ']':
            if (n == 0 || stack[--n] != '[') return false;
            break;
        case '}':
            if (n == 0 || stack[--n] != '{') return false;
            break;
        default:
            return false;
        }
        s++;
    }

    return n == 0;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Usage: ./test xxxx");
        exit(-1);
    }
    printf("%s\n", isValid(argv[1]) ? "true" : "false");
    return 0;
}