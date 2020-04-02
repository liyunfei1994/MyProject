/*
	2020年4月2日21:15:11
	二分查找算法
	二分查找的两个前提：
		1. 数组
		2. 有序存放
	二分查找的时间复杂度为O(logN)
*/

int BinarySearch(List Tbl, ElementType K)
{
	int left, right, mid, NoFound=-1;

	lef=1;
	right = Tbl->Length;
	while (left <= right)
	{
		mid = (left+right)/2;
		if (K<Tbl->Element[mid])
		{
			right=mid-1;
		}
		else if (K>Tbl->Element[mid])
		{
			left=mid+1;
		}
		else
		{
			return mid;
		}
	}

	return NoFound;
}
