/*
    2020年4月23日17:34:17
    继承
*/


#include<iostream>
using namespace std;

//基类 Pelple
class People{
public:
    void setname(char *name);
    void setage(int age);
    char *getname();
    int getage();
private:
    char *m_name;
    int m_age;
};
void People::setname(char *name){ m_name = name; }
void People::setage(int age){ m_age = age; }
char* People::getname(){ return m_name; }
int People::getage(){ return m_age;}

//派生类 Student
class Student: public People{
public:
    void setscore(float score);
    float getscore();
private:
    float m_score;
};

void Student::setscore(float score){ m_score = score; }
float Student::getscore(){ return m_score; }

int main(){
    Student stu;
    stu.setname("XiaoMing");
    stu.setage(16);
    stu.setscore(95.5f);
    cout<<stu.getname()<<", year is "<<stu.getage()<<", score is "<<stu.getscore()<<endl;

    return 0;
}
