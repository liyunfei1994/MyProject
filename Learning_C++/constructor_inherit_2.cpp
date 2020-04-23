/*
	2020年4月23日21:57:53
	基类构造函数的调用规则

	事实上，通过派生类创建对象时必须要调用基类的构造函数，
	这是语法规定。换句话说，定义派生类构造函数时最好指明基类构造函数；
	如果不指明，就调用基类的默认构造函数（不带参数的构造函数）；
	如果没有默认构造函数，那么编译失败。
*/

#include <iostream>
using namespace std;

//基类People
class People{
public:
    People();  //基类默认构造函数
    People(char *name, int age);
protected:
    char *m_name;
    int m_age;
};
People::People(): m_name("xxx"), m_age(0){ }
People::People(char *name, int age): m_name(name), m_age(age){}

//派生类Student
class Student: public People{
public:
    Student();
    Student(char*, int, float);
public:
    void display();
private:
    float m_score;
};
Student::Student(): m_score(0.0){ }  //派生类默认构造函数
Student::Student(char *name, int age, float score): People(name, age), m_score(score){ }
void Student::display(){
    cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<"."<<endl;
}

int main(){
    Student stu1;
    stu1.display();

    Student stu2("XiaoMing", 16, 90.5);
    stu2.display();

    return 0;
}

/*
创建对象 stu1 时，执行派生类的构造函数Student::Student()，
它并没有指明要调用基类的哪一个构造函数，从运行结果可以很明显地看出来，
系统默认调用了不带参数的构造函数，也就是People::People()。
xxx, year is 0, score is 0.
XiaoMing, year is 16, score is 90.5.
*/
