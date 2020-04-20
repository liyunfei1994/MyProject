/*
	2020年4月19日22:20:06
	友元函数和友元类

	将非成员函数声明为友元函数

	在 C++ 中，一个类中可以有 public、protected、private 三种属性的成员，
	通过对象可以访问 public 成员，
	只有本类中的函数可以访问本类的 private 成员。
	现在，我们来介绍一种例外情况——友元（friend）。
	借助友元（friend），
	可以使得其他类中的成员函数以及全局范围内的函数访问当前类的 private 成员。

	在 C++ 中，这种友好关系可以用 friend 关键字指明，
	中文多译为“友元”，借助友元可以访问与其有好友关系的类中的私有成员

	在当前类以外定义的、不属于当前类的函数也可以在类中声明，
	但要在前面加 friend 关键字，这样就构成了友元函数。

	友元函数可以是不属于任何类的非成员函数，也可以是其他类的成员函数。
	友元函数可以访问当前类中的所有成员，
	包括 public、protected、private 属性的。
*/

#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
public:
    friend void show(Student *pstu);  //将show()声明为友元函数
private:
    char *m_name;
    int m_age;
    float m_score;
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){ }

//非成员函数
//show() 是一个全局范围内的非成员函数，它不属于任何类，它的作用是输出学生的信息。
/*
m_name、m_age、m_score 是 Student 类的 private 成员，原则上不能通过对象访问，
但在 show() 函数中又必须使用这些 private 成员，所以将 show() 声明为 Student 类的友元函数。
友元函数不同于类的成员函数，在友元函数中不能直接访问类的成员，必须要借助对象
*/
void show(Student *pstu){
    cout<<pstu->m_name<<", year is "<<pstu->m_age<<", score is "<<pstu->m_score<<endl;
}

int main(){
    Student stu("XiaoMing", 15, 90.6);
    show(&stu);  //调用友元函数
    Student *pstu = new Student("LiLei", 16, 80.5);
    show(pstu);  //调用友元函数

    return 0;
}
