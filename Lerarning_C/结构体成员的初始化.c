#include <stdio.h>

#define NAME_LEN 64

struct student {
    char name[NAME_LEN];
    int height;
    float weight;
    long schols;
};

int main(void)
{
    struct student Gougou = {"Liyunfei", 180, 68, };

    printf("Gougou's name is %s\n", Gougou.name);
    printf("Gougou's height is %d\n", Gougou.height);
    printf("Gougou's height is %lf\n", Gougou.weight);
    printf("Gougou's schols is %ld\n", Gougou.schols);

    return 0;
}

没有赋初始值的会被初始化为0
