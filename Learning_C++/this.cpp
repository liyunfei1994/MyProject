/*
	2020年4月18日22:04:50
	this 指针

	this 是 C++ 中的一个关键字，也是一个 const 指针，
	它指向当前对象，通过它可以访问当前对象的所有成员。

	所谓当前对象，是指正在使用的对象。
	例如对于stu.show();，
	stu 就是当前对象，this 就指向 stu。

	this 是一个指针，要用->来访问成员变量或成员函数
*/

#include <iostream>
using namespace std;

class Student{
public:
    void setname(char *name);
    void setage(int age);
    void setscore(float score);
    void show();
    void printThis();
private:
    char *name;
    int age;
    float score;
};

void Student::setname(char *name){
    this->name = name;
}
void Student::setage(int age){
    this->age = age;
}
void Student::setscore(float score){
    this->score = score;
}
void Student::show(){
    cout<<this->name<<" year is "<<this->age<<", score is "<<this->score<<endl;
}

void Student::printThis(){
	cout<<this<<endl;
}

int main(){
	//本例中，this 的值和 pstu 的值是相同的。
    Student *pstu = new Student;
    pstu -> printThis();
    cout<<pstu<<endl;
    pstu -> setname("LiHua");
    pstu -> setage(16);
    pstu -> setscore(96.5);
    pstu -> show();

    Student *pstu_ = new Student;
    pstu_ -> printThis();
    cout<<pstu_<<endl;

    return 0;
}

/*
0xbd2e78
0xbd2e78
LiHua year is 16, score is 96.5
0xbd2f70
0xbd2f70

this 确实指向了当前对象，而且对于不同的对象，this 的值也不一样

1. this 是 const 指针，它的值是不能被修改的，
一切企图修改该指针的操作，如赋值、递增、递减等都是不允许的。
2. this 只能在成员函数内部使用，用在其他地方没有意义，也是非法的。
3. 只有当对象被创建后 this 才有意义，
因此不能在 static 成员函数中使用（后续会讲到 static 成员）。

this 实际上是成员函数的一个形参，
在调用成员函数时将对象的地址作为实参传递给 this。
不过 this 这个形参是隐式的，
它并不出现在代码中，
而是在编译阶段由编译器默默地将它添加到参数列表中。
*/
