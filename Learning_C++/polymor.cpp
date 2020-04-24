/*
	2020年4月24日21:30:44
	虚函数与多态

	基类的指针也可以指向派生类对象
*/

// #include <iostream>
// using namespace std;

// //基类People
// class People{
// public:
//     People(char *name, int age);
//     void display();
// protected:
//     char *m_name;
//     int m_age;
// };
// People::People(char *name, int age): m_name(name), m_age(age){}
// void People::display(){
//     cout<<m_name<<"This year "<<m_age<<" old, have no job."<<endl;
// }

// //派生类Teacher
// class Teacher: public People{
// public:
//     Teacher(char *name, int age, int salary);
//     void display();
// private:
//     int m_salary;
// };
// Teacher::Teacher(char *name, int age, int salary): People(name, age), m_salary(salary){}
// void Teacher::display(){
//     cout<<m_name<<" This year "<<m_age<<" old, is a teacher "<<m_salary<<" $"<<endl;
// }

// int main(){
//     People *p = new People("XiaoMing", 23);
//     p -> display();

//     p = new Teacher("LiHua", 45, 8200);
//     p -> display();

//     return 0;
// }

/*
如果指针指向了派生类对象，那么就应该使用派生类的成员变量和成员函数，
这符合人们的思维习惯。但是本例的运行结果却告诉我们，
当基类指针 p 指向派生类 Teacher 的对象时，
虽然使用了 Teacher 的成员变量，但是却没有使用它的成员函数，导致输出结果不伦不类

换句话说，通过基类指针只能访问派生类的成员变量，但是不能访问派生类的成员函数。

为了消除这种尴尬，让基类指针能够访问派生类的成员函数，
C++ 增加了虚函数（Virtual Function）。
使用虚函数非常简单，只需要在函数声明前面增加 virtual 关键字。

XiaoMingThis year 23 old, have no job.
LiHuaThis year 45 old, have no job.
*/

#include <iostream>
using namespace std;

//基类People
class People{
public:
    People(char *name, int age);
    virtual void display();  //声明为虚函数
protected:
    char *m_name;
    int m_age;
};
People::People(char *name, int age): m_name(name), m_age(age){}
void People::display(){
    cout<<m_name<<" this year "<<m_age<<", have no job."<<endl;
}

//派生类Teacher
class Teacher: public People{
public:
    Teacher(char *name, int age, int salary);
    virtual void display();  //声明为虚函数
private:
    int m_salary;
};
Teacher::Teacher(char *name, int age, int salary): People(name, age), m_salary(salary){}
void Teacher::display(){
    cout<<m_name<<" this year "<<m_age<<", is a teacher "<<m_salary<<"$"<<endl;
}

int main(){
    People *p = new People("XiaoMing", 23);
    p -> display();

    p = new Teacher("LiHua", 45, 8200);
    p -> display();

    return 0;
}

/*
有了虚函数，基类指针指向基类对象时就使用基类的成员（包括成员函数和成员变量），
指向派生类对象时就使用派生类的成员。
换句话说，基类指针可以按照基类的方式来做事，
也可以按照派生类的方式来做事，它有多种形态，
或者说有多种表现方式，我们将这种现象称为多态（Polymorphism）。

同样是p->display();这条语句，当 p 指向不同的对象时，
它执行的操作是不一样的。同一条语句可以执行不同的操作，
看起来有不同表现方式，这就是多态。

多态是面向对象编程的主要特征之一，C++中虚函数的唯一用处就是构成多态。

C++提供多态的目的是：
可以通过基类指针对所有派生类（包括直接派生和间接派生）的成员变量和成员函数进行“全方位”的访问，
尤其是成员函数。如果没有多态，我们只能访问成员变量。

XiaoMing this year 23, have no job.
LiHua this year 45, is a teacher 8200$
*/
