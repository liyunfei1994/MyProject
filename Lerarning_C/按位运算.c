#include <stdio.h>

int count_bits(unsigned x)
{
    int bits=0;
    while (x){
        if (x & 1U){
            bits ++;
        }
        x >>= 1;
    }

    return bits;
}

int int_bits(void)
{
    return count_bits(~0U);
}
void print_bits(unsigned x)
{
    int i;

    for (i = int_bits()-1; i >= 0; i--){
        putchar(((x >> i) & 1U) ? '1':'0');
    }
}

int main(void)
{
    unsigned a, b;

    printf("Please enter two positive number:\n");
    printf("a:");   scanf("%u", &a);
    printf("b:");   scanf("%u", &b);
    
    printf("\n a = ");  print_bits(a);
    printf("\n b = ");  print_bits(b);

    printf("\n a & b = ");  print_bits(a&b);
    printf("\n a | b = ");  print_bits(a|b);
    printf("\n a ^ b = ");  print_bits(a^b);
    printf("\n ~a = ");     print_bits(~a);
    printf("\n ~b = ");     print_bits(~b);
    putchar('\n');

    return 0;
    
}

Please enter two positive number:
a:15
b:10

 a = 00000000000000000000000000001111
 b = 00000000000000000000000000001010
 a & b = 00000000000000000000000000001010
 a | b = 00000000000000000000000000001111
 a ^ b = 00000000000000000000000000000101
 ~a = 11111111111111111111111111110000
 ~b = 11111111111111111111111111110101
