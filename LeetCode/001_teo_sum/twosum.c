#include <stdio.h>
#include <stdlib.h>

typedef struct object
{
    int val;
    int index;
}OBJECT, *POBJECT;


static int compare(const void *a, const void *b)
{
    return ((POBJECT)a)->val - ((POBJECT)b)->val;
}


/*
qsort函数(全称quicksort)。它是ANSI C标准中提供的，其声明在stdlib.h文件中
是根据二分法写的，其时间复杂度为n*log(n)

参数：  1 待排序数组，排序之后的结果仍放在这个数组中
        2 数组中待排序元素数量
        3 各元素的占用空间大小（单位为字节）
        4 指向函数的指针，用于确定排序的顺序（需要用户自定义一个比较函数）

*/

static int * twosum(int *nums, int numsSize, int target, int *returnSize)
{
    int i, j;
    // struct object *objs = malloc(numsSize * sizeof(*objs));
    POBJECT objs = malloc(numsSize * sizeof(OBJECT));
    for (i = 0; i < numsSize; i++) {
        objs[i].val = nums[i];
        objs[i].index = i;
    }
    qsort(objs, numsSize, sizeof(OBJECT), compare);
    printf("After qsort:\n");

    for (i=0; i < numsSize; i++){
        printf("val = %d\t", objs[i].val);
        printf("index = %d\n", objs[i].index);
    }
    
    int *results = malloc(2 * sizeof(int));
    
    i = 0;
    j = numsSize - 1;
    while (i < j) {
        int sum = objs[i].val + objs[j].val;
        if (sum < target) {
            i++;
        } else if (sum > target) {
            j--;
        } else {
            results[0] = objs[i].index;
            results[1] = objs[j].index;
            *returnSize = 2;
            return results;
        }
    }
    return NULL;
}

int main(void)
{
    
    int i;
    int nums[] = {2, 1, 3, 4};
    int size = sizeof(nums) / sizeof(*nums);
    printf("The original array is: \n");
    for (i = 0; i < size; i++){
        printf("%d  ",nums[i]);
    }
    printf("numsize = %d\t", size);

    int target = 6;
    printf("Target is %d\n", target);
    int count = 0;
    int *indexes = twosum(nums, size, target, &count);

    if (indexes != NULL) {
        printf("The indexes are %d and %d\n", indexes[0], indexes[1]);
    } else {
        printf("Not found\n");
    }

    return 0;
}

The original array is:
2  1  3  4  numsize = 4 Target is 6
After qsort:
val = 1 index = 1
val = 2 index = 0
val = 3 index = 2
val = 4 index = 3
The indexes are 0 and 3
