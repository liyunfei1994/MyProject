/*
	2020年4月18日16:31:59
	C++的构造函数

	在C++中，有一种特殊的成员函数，
	它的名字和类名相同，没有返回值，
	不需要用户显式调用（用户也不能调用），
	而是在创建对象时自动执行。
	这种特殊的成员函数就是构造函数（Constructor）。


*/

// #include <iostream>
// using namespace std;

// class Student{
// private:
//     char *m_name;
//     int m_age;
//     float m_score;
// public:
//     //声明构造函数
//     //构造函数必须是 public 属性的，否则创建对象时无法调用。
//     //构造函数没有返回值
//     Student(char *name, int age, float score);
//     //声明普通成员函数
//     void show();
// };

// //定义构造函数
// Student::Student(char *name, int age, float score){
//     m_name = name;
//     m_age = age;
//     m_score = score;
// }
// //定义普通成员函数
// void Student::show(){
//     cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<endl;
// }

// int main(){
//     //创建对象时向构造函数传参
//     Student stu("XiaoMing", 15, 92.5f);
//     stu.show();
//     //创建对象时向构造函数传参
//     Student *pstu = new Student("LiHua", 16, 96);
//     pstu -> show();

//     return 0;
// }

/*
XiaoMing, year is 15, score is 92.5
LiHua, year is 16, score is 96
*/

//-------------------------------------
//构造函数的重载


#include <iostream>
using namespace std;

class Student{
private:
    char *m_name;
    int m_age;
    float m_score;
public:
    Student();
    Student(char *name, int age, float score);
    void setname(char *name);
    void setage(int age);
    void setscore(float score);
    void show();
};

Student::Student(){
    m_name = NULL;
    m_age = 0;
    m_score = 0.0;
}
Student::Student(char *name, int age, float score){
    m_name = name;
    m_age = age;
    m_score = score;
}
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
    if(m_name == NULL || m_age <= 0){
        cout<<"NO initialize"<<endl;
    }else{
        cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<endl;
    }
}

int main(){
    //调用构造函数 Student(char *, int, float)
    Student stu("XiaoMing", 15, 92.5f);
    stu.show();

    //调用构造函数 Student()
    Student *pstu = new Student();
    pstu -> show();
    pstu -> setname("LiHua");
    pstu -> setage(16);
    pstu -> setscore(96);
    pstu -> show();

    return 0;
}
/*
XiaoMing, year is 15, score is 92.5
NO initialize
LiHua, year is 16, score is 96
*/
