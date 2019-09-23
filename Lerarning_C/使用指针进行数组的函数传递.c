/*
    数组的传递
*/

#include <stdio.h>

// void ary_set(int v[10], int n, int val)
// {
//     int i;
//     for (i = 0; i < n; i++){
//         v[i] = val;
//     }
// }
void ary_set(int *v, int n, int val)
{             //形参v的类型不是数组，而是指针，即使写成v[100]也没有用
    int i;
    for (i = 0; i < n; i++){
        v[i] = val;     //在内部，可以像数组一样使用指针。
    }
}

int main(void)
{
    int i;
    int a[]={1,2,3,4,5};

    ary_set(a, 5, 99);   //在传递数组的时候，有必要将其元素个数作为别的参数来处理
    for (i=0; i < 5; i++){
        printf("a[%d]=%d\n", i, a[i]);
    }
}

a[0]=99
a[1]=99
a[2]=99
a[3]=99
a[4]=99
