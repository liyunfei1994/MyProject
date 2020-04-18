/*
	2020年4月18日15:47:13
	C++的内存模型

	编译器会将成员变量和成员函数分开存储：
	分别为每个对象的成员变量分配内存，
	但是所有对象都共享同一段函数代码。

	成员变量在堆区或栈区分配内存，成员函数在代码区分配内存。
*/

#include <iostream>
using namespace std;

class Student{
public:
    char *m_name;
    int m_age;
    float m_score;
public:
    void setname(char *name);
    void setage(int age);
    void setscore(float score);
    void show();
};

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
    cout<<sizeof(stu)<<endl;
    //在堆上创建对象
    Student *pstu = new Student();
    cout<<sizeof(*pstu)<<endl;
    //类的大小
    cout<<sizeof(Student)<<endl;

    cout<<&(pstu->m_name)<<endl;
    cout<<&(pstu->m_age)<<endl;
    cout<<&(pstu->m_score)<<endl;

    return 0;
}

/*
Student 类包含三个成员变量，
它们的类型分别是 char *、int、float，
都占用 4 个字节的内存，
加起来共占用 12 个字节的内存。
通过 sizeof 求得的结果等于 12，
恰好说明对象所占用的内存仅仅包含了成员变量。
12
12
12
0x732e80
0x732e84
0x732e88
*/
