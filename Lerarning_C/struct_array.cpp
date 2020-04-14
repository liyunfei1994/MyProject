/*
	2020年4月14日10:17:18
	结构体数组
	所谓结构体数组，是指数组中的每个元素都是一个结构体

	定义结构体数组的方式：
	struct stu
	{
		char *name;
		int num;
		int age;
	} class[5];
	表示一个班级有5个学生。

	结构体数组在定义的同时也可以初始化完成
	struct stu
	{
		char *name;
		int num;
		int age;
	} class[5] = 
		{
			{"li ping", 5, 18}，
			{"zhang ping", 4, 19},
			....;
			....;
			....;
		};
*/

#include <stdio.h>

struct{
    char *name;  //姓名
    int num;  //学号
    int age;  //年龄
    char group;  //所在小组
    float score;  //成绩
} Banji[] = {
    {"Li ping", 5, 18, 'C', 145.0}, //注意这里是逗号
    {"Zhang ping", 4, 19, 'A', 130.5},
    {"He fang", 1, 18, 'A', 148.5},
    {"Cheng ling", 2, 17, 'F', 139.0},
    {"Wang ming", 3, 17, 'B', 144.5}
};

//计算全班学生的总成绩，平均成绩以及140分以下的人数
int main(){
    int i, num_140 = 0;
    float sum = 0;
    for(i=0; i<5; i++)
    {
        sum += Banji[i].score;
        if(Banji[i].score < 140) 
        {
        	num_140++;
        }	
    }
    printf("sum=%.2f\naverage=%.2f\nnum_140=%d\n", sum, sum/5, num_140);
    return 0;
}
