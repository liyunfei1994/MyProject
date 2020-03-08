# include <stdio.h>

long f(long n)
{
	if (1 == n)
		return 1;
	else
		return f(n-1) * n;
}

long sum(int n)
{
	if (1 == n)
		return 1;
	else
		return n + sum(n-1);
}

int main(void)
{
	printf("%d\n", f(100));

	printf("%d\n", sum(100));

	return 0;
}

--------------------
--------------------

0
5050
