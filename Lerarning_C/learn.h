#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct mystruct{
	int age;
	double score;
	// char name[20];
	mystruct(int Age, double Score)
	:age(Age),
	score(Score){
		printf("%s\n", "This constructor!");
	};  //有没有这个结尾的分号，好像没有影响……不会报错
};    //结构体末尾的分号不可以省略
