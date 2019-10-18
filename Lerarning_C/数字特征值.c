#include <math.h>
#include <stdio.h>
#include <stdlib.h>


int main(){
    int i;  // 读入的数
    int num=1;   //  表示数位
    int a;       //  表示数字从右向左分解的余数
    int t;       //  分解只有的数字
    int sum=0;   //  十进制的和
    int g;      //二进制的和

    scanf("%d", &i);

    t = i;
    // printf("t=%d\n", t);
    a = i%10;
    // printf("a=%d\n", a);
    // printf("======\n");
    while (t >= 1){
        if (a%2 == num%2){
            // printf("consistent!!");
            g = pow(2, num-1);
            // printf("g=%d\n", g);
            sum += g;
            // printf("sum=%d\n",sum);
        }
        num ++;
        // printf("num=%d\n", num);
        t /= 10;
        // printf("t=%d\n", t);
        a = t%10;
        // printf("a=%d\n", a);
        // printf("======\n");
    }
    printf("%d", sum);

    return 0;
}

342315
13
