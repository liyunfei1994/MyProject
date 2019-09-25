/*
    用表示学生的结构体来显示学生的信息
*/

#include <stdio.h>
#include <string.h>

#define NAME_LEN 64

struct student {
    char name[NAME_LEN];
    int height;
    float weight;
    long schols;
};

int main(void)
{
    struct student Goudan;

    strcpy(Goudan.name, "Liyunfei");

    Goudan.height = 180;
    Goudan.weight = 68.2;
    Goudan.schols = 10000;

    printf("Goudan's name = %s\n", Goudan.name);
    printf("Goudan's height = %d\n", Goudan.height);
    printf("Goudan's weight = %.lf\n", Goudan.weight);
    printf("Goudan's schols = %ld\n", Goudan.schols);

    return 0;
}

Goudan's name = Liyunfei
Goudan's height = 180
Goudan's weight = 68
Goudan's schols = 10000
