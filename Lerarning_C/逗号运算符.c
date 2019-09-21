#include <stdio.h>

#define puts_alert(str)  (putchar('\a'), puts(str))

int main(void)
{
    int n;

    printf("Please enter an number:");
    scanf("%d", &n);

    if (n){
        puts_alert("This is not zero!");
    }else{
        puts_alert("This is zero!");
    }

    return 0;
}

a,b 按顺序判断a 和 b， 整个表达式最终生成b的判断结果

Please enter an number:98
This is not zero!
