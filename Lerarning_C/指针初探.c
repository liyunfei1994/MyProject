#include <stdio.h>

int main(void)
{
	int xiaoming =170;
	int gougou =180;
	int doudou  = 190;
	
	int *A,*B;  //变量名前带有*号，表示这是指针变量
				//A这个指针变量里，存放的是int型数据的地址
	
	A = &xiaoming;  //将小明的地址取出来，放在A中
	                //取址运算符，生成指针
					//表达式&xiaoming 是指向xiaoming的指针
					//其值是xiaoming 的地址
	B =&doudou;   //将豆豆的地址取出来，放在B中

	printf("xiaoming --> %d\n", xiaoming);  //170
	printf("gougou --> %d\n", gougou); 		//180
	printf("doudou --> %d\n", doudou);		//190
	printf("A point to xiaoming\n");
	printf("A the like person's height is :%d\n", *A);
	                        // *是指针运算符， 也被称为间接访问运算符
							//将*放在指针前面，就可以显示该指针指向的地方的内容
	printf("B point to doudou\n");
	printf("B the like person's height is :%d\n", *B);
	
	A = &gougou;     //将指向其他对象的指针赋给指针变量
					//指针变量就会指向新的对象
	puts("Change the doudou's height");
	//直接在这里修改 B指向对象的值
	//B 指向doudou, *B就是doudou的别名
	*B = 200;
	
	putchar('\n');
	puts("all changed!! A point to gougou");
	printf("xiaoming's height is :%d\n", xiaoming);
	printf("gougou's height is :%d\n", gougou);
	printf("doudou's height is :%d\n", doudou);
	printf("A the like person's height is :%d\n", *A);
	printf("B the like person's height is :%d\n", *B);
	
	return 0;
 } 
