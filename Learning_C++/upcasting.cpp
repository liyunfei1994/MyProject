/*
	2020年4月24日18:15:50
	C++ 向上转型

	类其实也是一种数据类型，也可以发生数据类型转换，
	不过这种转换只有在基类和派生类之间才有意义，
	并且只能将派生类赋值给基类，
	包括将派生类对象赋值给基类对象、
	将派生类指针赋值给基类指针、
	将派生类引用赋值给基类引用，
	这在 C++ 中称为向上转型（Upcasting）。
	相应地，将基类赋值给派生类称为向下转型（Downcasting）。

	向上转型非常安全，可以由编译器自动完成；向下转型有风险，需要程序员手动干预。

	向上转型和向下转型是面向对象编程的一种通用概念，
	它们也存在于 Java、C# 等编程语言中。


*/

#include <iostream>
using namespace std;

//基类
class A{
public:
    A(int a);
public:
    void display();
public:
    int m_a;
};
A::A(int a): m_a(a){ }
void A::display(){
    cout<<"Class A: m_a="<<m_a<<endl;
}

//派生类
class B: public A{
public:
    B(int a, int b);
public:
    void display();
public:
    int m_b;
};
B::B(int a, int b): A(a), m_b(b){ }
void B::display(){
    cout<<"Class B: m_a="<<m_a<<", m_b="<<m_b<<endl;
}


int main(){
    A a(10);
    B b(66, 99);
    //赋值前
    a.display();
    b.display();
    cout<<"--------------"<<endl;
    //赋值后
    //将派生类对象 赋值给基类对象
    /*
	赋值的本质是将现有的数据写入已分配好的内存中，
	对象的内存只包含了成员变量，所以对象之间的赋值是成员变量的赋值，成员函数不存在赋值问题。
	虽然有a=b;这样的赋值过程，
	但是 a.display() 始终调用的都是 A 类的 display() 函数。
	换句话说，对象之间的赋值不会影响成员函数，也不会影响 this 指针。
	将派生类对象赋值给基类对象时，会舍弃派生类新增的成员，也就是“大材小用”
    */
    a = b;
    a.display();
    b.display();

    return 0;
}

/*
这种转换关系是不可逆的，只能用派生类对象给基类对象赋值，而不能用基类对象给派生类对象赋值。
Class A: m_a=10
Class B: m_a=66, m_b=99
--------------
Class A: m_a=66
Class B: m_a=66, m_b=99
*/
