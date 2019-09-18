#include <stdio.h>

int scan_pint(void)
{
    int tmp;
    do {
        printf("Please enter an positive number:");
        scanf("%d", &tmp);
        if(tmp < 0){
            puts("\a Please do not enter an negative number.");
        }
    }while(tmp <= 0);

    return tmp;
}

int rev_int(int num)
{
    int tmp = 0;
    if(num > 0){
        do{
            tmp = tmp * 10 + num % 10;
            num /= 10;
        }while(num > 0);
    }
    return tmp;
}

int main(void)
{
    int nx = scan_pint();
    printf("After reverse, the number is:%d\n", rev_int(nx));

    return 0;
}
==============================================
#include <stdio.h>

int rev_int(int num)
{
    int tmp = 0;
    if(num > 0){
        do{
            tmp = tmp * 10 + num % 10;
            num /= 10;
        }while(num > 0);
    }
    return tmp;
}

int main(void)
{
    int tmp, nx;
    scanf("%d", &tmp );
    nx = rev_int(tmp);
    printf("%d", nx);
    return 0;
}
