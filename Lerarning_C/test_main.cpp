#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int isPrime(int n);

int main(int argc, const char *argv[]){
    int i, n, result;
    if(argc <= 1){
        printf("Error: no input integer!\n");
        exit(EXIT_SUCCESS);
    }
    for(i=1; i<argc; i++){
        n = atoi(argv[i]);
        result = isPrime(n);
        if(result < 0){
            printf("%3d is error.\n", n);
        }else if(result){
            printf("%3d is prime number.\n", n);
        }else{
            printf("%3d is not prime number.\n", n);
        }
    }
    return 0;
}

//判断是否是素数
int isPrime(int n){
    int i, j;
    if(n <= 1){  //参数错误
        return -1;
    }else if(n == 2){  //2是特例，单独处理
        return 1;
    }else if(n % 2 == 0){  //偶数不是素数
        return 0;
    }else{  //判断一个奇数是否是素数
        j = (int)sqrt(n);
        for(i=3; i<=j; i+=2){
            if (n % i == 0){
                return 0;
            }
        }
        return 1;
    }
}

--------------------------
D:\C\data structure>test_main -1 2 3 4 5 6
 -1 is error.
  2 is prime number.
  3 is prime number.
  4 is not prime number.
  5 is prime number.
  6 is not prime number.
  
/*
	2020年4月13日20:14:21
	main函数的高级用法：接受用户输入的数据
*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
	/*
		agrc 表示传递的字符串的数目
		argv 是一个指针数组，每个指针指向一个字符串
	*/

	int i;
	printf("The program receives %d parameters:\n", argc);

	for (i = 0; i < argc; ++i)
	{
		printf("%s\n", argv[i]);
	}

	return 0;
}

/*
D:\C\data structure>test.exe liyunfei wenchuanyi hahahaha
The program receives 4 parameters:
test.exe
liyunfei
wenchuanyi
hahahaha
*/
