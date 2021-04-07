/*
    用于确认单精度浮点数的表示方法
*/

#include <stdio.h>
#include <string.h>


void main()
{
    float data;
    unsigned long buff;
    int i;
    char s[34];

    // 将0.75以单精度浮点数的形式存储在变量data中 
    data = (float)0.75;
    // 将数据复制到4字节长度的整数变量buff中以逐个提取出每一位 
    memcpy(&buff, &data, 4);
    // 逐一提取出每一位
    for (i = 33; i >= 0; i--)
    {
        if (i == 1 || i == 10)
        {
            // 加入破折号来区分符号部分、指数部分以及尾数部分
            s[i] = '-';
        }
        else
        {
            // 判断数字是奇数还是偶数，来判断末尾的数字是0还是1
            if (buff % 2 == 1)
            {
                s[i] = '1';
            }
            else
            {
                {
                    s[i] = '0';
                }
            }
            buff /= 2;
        }
    }
    s[34] = '\0';

    printf("%s\n", s);
}

/*
0-01111110-10000000000000000000000
*/
