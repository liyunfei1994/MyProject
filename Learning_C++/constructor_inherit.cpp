/*
	2020年4月23日21:41:04
	基类和派生类的构造函数

	前面我们说基类的成员函数可以被继承，
	可以通过派生类的对象访问，
	但这仅仅指的是普通的成员函数，
	类的构造函数不能被继承。
	构造函数不能被继承是有道理的，因为即使继承了，
	它的名字和派生类的名字也不一样，不能成为派生类的构造函数，
	当然更不能成为普通的成员函数。

	在设计派生类时，对继承过来的成员变量的初始化工作也要由派生类的构造函数完成，
	但是大部分基类都有 private 属性的成员变量，
	它们在派生类中无法访问，更不能使用派生类的构造函数来初始化。

	这种矛盾在C++继承中是普遍存在的，解决这个问题的思路是：
	在派生类的构造函数中调用基类的构造函数。

*/

#include<iostream>
using namespace std;

//基类People
class People{
protected:
    char *m_name;
    int m_age;
public:
    People(char*, int);
};
People::People(char *name, int age): m_name(name), m_age(age){}

//派生类Student
class Student: public People{
private:
    float m_score;
public:
    Student(char *name, int age, float score);
    void display();
};
//People(name, age)就是调用基类的构造函数
Student::Student(char *name, int age, float score): People(name, age), m_score(score){ }
void Student::display(){
    cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<"."<<endl;
}

int main(){
    Student stu("XiaoMing", 16, 90.5);
    stu.display();

    return 0;
}

/*
XiaoMing, year is 16, score is 90.5.
*/
