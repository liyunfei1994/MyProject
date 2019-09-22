/*
	读取学生的身高并排序
*/

#include <stdio.h>

#define NUMBER 5

// 按照升序进行排列
void bsort(int a[], int n)
{
	int i, j;

	for (i =0; i < n-1; i++){   //数组里一共有n个数,则遍历n-1趟
		for (j=n-1; j>i; j--){   //从数组的末尾向开头进行遍历
			if (a[j-1]>a[j]){    //如果发现前一个数比后一个数大
				int temp = a[j];   //则交换两个数的位置
				a[j] = a[j-1];
				a[j-1] = temp;
			}
		}
	}
}


int main(void)
{
	int i;
	int height[NUMBER];

	printf("Please enter %d persons height\n", NUMBER);
	for (i = 0; i < NUMBER; i++){
		printf("NO.%2d:", i+1);
		scanf("%d", &height[i]);
	}

	bsort(height, NUMBER);
	puts("The sort is :");

	for (i=0; i < NUMBER; i++){
		printf("NO.%2d: %d \n", i+1, height[i]);
	}

	return 0;

}
