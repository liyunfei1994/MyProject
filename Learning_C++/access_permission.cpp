/*
	2020年4月18日14:11:27
	C++ 类成员的访问权限

	C++通过 public、protected、private 
	三个关键字来控制成员变量和成员函数的访问权限，
	它们分别表示公有的、受保护的、私有的，
	被称为成员访问限定符。
	所谓访问权限，就是你能不能使用该类中的成员。

	Java、C# 程序员注意，
	C++ 中的 public、private、protected 只能修饰类的成员，
	不能修饰类，
	C++中的类没有共有私有之分。

	在类的内部（定义类的代码内部），
	无论成员被声明为 public、protected 还是 private，
	都是可以互相访问的，
	没有访问权限的限制。

	在类的外部（定义类的代码之外），
	只能通过对象访问成员，
	并且通过对象只能访问 public 属性的成员，
	不能访问 private、protected 属性的成员。

    只在类体中声明函数，而将函数定义放在类体外面

    当成员函数定义在类外时，就必须在函数名前面加上类名予以限定。
    ::被称为域解析符（也称作用域运算符或作用域限定符），
    用来连接类名和函数名，指明当前函数属于哪个类。

    成员函数必须先在类体中作原型声明，
    然后在类外定义，也就是说类体的位置应在函数定义之前。

    在类体中和类体外定义成员函数是有区别的：
    在类体中定义的成员函数会自动成为内联函数，在类体外定义的不会。

    内联函数一般不是我们所期望的，它会将函数调用处用函数体替代，
    所以我建议在类体内部对成员函数作声明，
    而在类体外部进行定义，这是一种良好的编程习惯，
    实际开发中大家也是这样做的。
*/

#include <iostream>
using namespace std;

//类的声明
class Student{
private:  //私有的
    /*
    成员变量大都以m_开头，这是约定成俗的写法，
    不是语法规定的内容。
    以m_开头既可以一眼看出这是成员变量，
    又可以和成员函数中的形参名字区分开。
    */
    char *m_name;
    int m_age;
    float m_score;

public:  //共有的
    void setname(char *name);
    void setage(int age);
    void setscore(float score);
    void show();
};

//成员函数的定义
void Student::setname(char *name){
    m_name = name;
}
void Student::setage(int age){
    m_age = age;
}
void Student::setscore(float score){
    m_score = score;
}
void Student::show(){
    cout<<m_name<<" year is "<<m_age<<", score is "<<m_score<<endl;
}

int main(){
    //在栈上创建对象
    Student stu;
    stu.setname("Xiaoming");
    stu.setage(15);
    stu.setscore(92.5f);
    stu.show();

    //在堆上创建对象
    Student *pstu = new Student;
    pstu -> setname("LiHua");
    pstu -> setage(16);
    pstu -> setscore(96);
    pstu -> show();

    return 0;
}

