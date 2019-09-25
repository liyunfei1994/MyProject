#include <stdio.h>

#define NAME_LEN   64

struct student{
    char name[NAME_LEN];
    int height;
    float weight;
    long schols;
};

void change(struct student *std){
    // if ((*std).height < 180){
    //     (*std).height = 180;
    // }
    // if ((*std).weight > 80){
    //     (*std).weight = 80;
    // }
    if (std->height < 180){
        std->height = 180;
    }
    // 箭头运算符
    if (std->weight > 80){
        std->weight = 80;
    }

}

int main(void)
{
    struct student Gougou = {"Liyunfei", 170, 90, 10000};

    change(&Gougou);

    printf("Gougou's name is %s\n", Gougou.name);
    printf("Gougou's height is %d\n", Gougou.height);
    printf("Gougou's height is %lf\n", Gougou.weight);
    printf("Gougou's schols is %ld\n", Gougou.schols);

    return 0;
}
Gougou's name is Liyunfei
Gougou's height is 180
Gougou's height is 80.000000
Gougou's schols is 10000
