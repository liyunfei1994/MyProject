#include <stdio.h>

#define NUMBER 5
#define FAILED -1

int search(int v[], int key, int n)
{
    int i = 0;
    v[n] = key;
    while (1) {
        if (v[i] == key){
            break;
        }
        i++;
    }

    return (i < n)? i: FAILED;
}

int main(void)
{
    int i, ky, idx;

    int vx[NUMBER+1];

    for (i=0; i<NUMBER; i++){
        printf("vx[%d]:", i);
        scanf("%d", &vx[i]);
    }

    printf("You want find:");
    scanf("%d", &ky);

    if ((idx = search(vx, ky, NUMBER)) == FAILED){
        puts("\a Can't find it!");
    }else
    {
        printf("%d is the N0.%d number.", ky, idx+1);
    }
    
    return 0;
}

vx[0]:12
vx[1]:23
vx[2]:34
vx[3]:45
vx[4]:56
You want find:21
 Can't find it!
 
vx[0]:12
vx[1]:23
vx[2]:34
vx[3]:45
vx[4]:56
You want find:23
23 is the N0.2 number.
