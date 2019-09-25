#include <stdio.h>

struct xyz{
    int x;
    long y;
    double z;
};

struct xyz xyz_off(int x, long y, double z){
    struct xyz temp;

    temp.x = x;
    temp.y = y;
    temp.z = z;

    return temp;
}

int main(void)
{
    struct xyz s = {0, 0, 0};

    s = xyz_off(12, 700, 900);

    printf("xyz.x = %d\n", s.x);
    printf("xyz.y = %ld\n", s.y);
    printf("xyz.z = %f\n", s.z);

    return 0;
}


xyz.x = 12
xyz.y = 700
xyz.z = 900.000000
