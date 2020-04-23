/*
    2020年4月23日19:59:22
    改变访问权限

    使用 using 关键字可以改变基类成员在派生类中的访问权限，
    例如将 public 改为 private、将 protected 改为 public。

    using 只能改变基类中 public 和 protected 成员的访问权限，
    不能改变 private 成员的访问权限


*/


#include<iostream>
using namespace std;

//基类People
class People {
public:
    void show();
protected:
    //protected 成员不能通过对象访问
    char *m_name;
    int m_age;
};
void People::show() {
    cout << m_name << ", year is " << m_age << endl;
}

//派生类Student
class Student : public People {
public:
    void learning();
public:
    using People::m_name;  //将protected改为public
    using People::m_age;  //将protected改为public
    float m_score;
private:
    using People::show;  //将public改为private
};
void Student::learning() {
    cout << "I'm " << m_name << ", " << m_age << "years old, I got" << m_score << "!" << endl;
}

int main() {
    Student stu;
    //对象访问成员，必须改为public成员
    stu.m_name = "XiaoMing";
    stu.m_age = 16;
    stu.m_score = 99.5f;
    // stu.show();  //compile error
    stu.learning();

    return 0;
}
