#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100000

//时间复杂度O(N^3) --2ms
//100 个随机整数 --1ms
//1000个随机整数 --445ms
int MaxSubseqSum1(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j, k;
	for (i = 0; i < N; i++)  //i是子列左端位置
	{
		for(j = i; j < N; j++)  //j是子列右端位置
		{
			ThisSum = 0;     //ThisSum是从A[i]-A[j]的子列和
			for (k = i; k <= j; k++)   //子列的长度由k控制
			{
				ThisSum += A[k];
			}
			if (ThisSum > MaxSum)
			{
				MaxSum = ThisSum;  //如果刚得到的子列和比MaxSum大
								   //则更新结果
			}
		}
	}

	return MaxSum;
}

//时间复杂度O(N^2) --1ms
//100个随机整数 --2ms
//1000个随机整数 --3ms
//10000个随机整数 --41ms
//100000个随机数  --3760ms
int MaxSubseqSum2(int A[], int N)
{
	int ThisSum, MaxSum=0;
	int i, j;

	for (i = 0; i < N; ++i)  //i 是子列左端位置
	{
		ThisSum = 0;
		for (j = i; j < N; ++j)    //j 是子列右端位置
		{
			ThisSum += A[j];   //对于相同的i,不同的j，
								//只需要在j-1的基础上加上A[j]即可
			if (ThisSum > MaxSum)
			{
				MaxSum = ThisSum;
			}
		}
	}

	return MaxSum;
}

//分治法，时间复杂度 O(NlogN)
/*返回三个整数的最大值*/ 
int Max3(int A, int B, int C) {								
	return (A > B) ? (A > C ? A : C) : (B > C ? B : C); 
}

//算法4， 在线处理，时间复杂度O(N)
//100个随机数 --3ms
//1000个随机数  --3ms
//10000个随机数  --4ms
//100000个随机数 --17ms
int MaxSubseqSum4(int A[], int N)
{
	int ThisSum, MaxSum;
	int i;
	ThisSum = MaxSum = 0;
	for (i = 0; i < N; ++i)
	{
		ThisSum += A[i];
		if (ThisSum > MaxSum)
		{
			MaxSum = ThisSum;
		}
		else if (ThisSum < 0)
		{
			ThisSum = 0;
		}
	}

	return MaxSum;
}

int main()
{
	int n, i;
	int begintime, endtime;
	int a[MAX] = {0};
	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		//a[i] = rand();
		scanf("%d", &a[i]);
	}
	begintime = clock();
	printf("%d\n", MaxSubseqSum4(a, n));
	endtime = clock();
	printf("Running Time: %d ms\n", endtime-begintime);
	return 0;
}
