/*
	2020年4月19日21:47:21
	const 对象

	在 C++ 中，const 也可以用来修饰对象，称为常对象。
	一旦将对象定义为常对象之后，
	就只能调用类的 const 成员（包括 const 成员变量和 const 成员函数）了。

*/

#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
public:
    void show();
    char *getname() const;
    int getage() const;
    float getscore() const;
private:
    char *m_name;
    int m_age;
    float m_score;
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){ }
void Student::show(){
    cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<endl;
}
char * Student::getname() const{
    return m_name;
}
int Student::getage() const{
    return m_age;
}
float Student::getscore() const{
    return m_score;
}

int main(){
    const Student stu("XiaoMing", 15, 90.6);
    // stu.show();  //error
    cout<<stu.getname()<<", year is "<<stu.getage()<<", socre is "<<stu.getscore()<<endl;

    const Student *pstu = new Student("LiLei", 16, 80.5);
    //pstu -> show();  //error
    cout<<pstu->getname()<<", year is "<<pstu->getage()<<", score is "<<pstu->getscore()<<endl;

    return 0;
}
