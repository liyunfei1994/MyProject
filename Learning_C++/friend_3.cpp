/*
	2020年4月20日17:31:22
	友元类
	
	不仅可以将一个函数声明为一个类的“朋友”，
	还可以将整个类声明为另一个类的“朋友”，
	这就是友元类。
	友元类中的所有成员函数都是另外一个类的友元函数。
*/

#include <iostream>
using namespace std;

class Address;  //提前声明Address类

//声明Student类
class Student{
public:
    Student(char *name, int age, float score);
public:
    void show(Address *addr);
private:
    char *m_name;
    int m_age;
    float m_score;
};

//定义ddress类
class Address{
public:
    Address(char *province, char *city, char *district);
public:
    //将Student类声明为Address类的友元类
    friend class Student;
private:
    char *m_province;  //省份
    char *m_city;  //城市
    char *m_district;  //区（市区）
};

//实现Student类
Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){ }
void Student::show(Address *addr){
    cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<endl;
    cout<<"Address: "<<addr->m_province<<" province "<<addr->m_city<<" city "<<addr->m_district<<" district "<<endl;
}

//实现Address类
Address::Address(char *province, char *city, char *district){
    m_province = province;
    m_city = city;
    m_district = district;
}

int main(){
    Student stu("XiaoMing", 16, 95.5f);
    Address addr("Shanxi", "xian", "yanta");
    stu.show(&addr);
   
    Student *pstu = new Student("LiLei", 16, 80.5);
    Address *paddr = new Address("HeBei", "HengShui", "TaoCheng");
    pstu -> show(paddr);

    return 0;
}

/*
XiaoMing, year is 16, score is 95.5
Address: Shanxi province xian city yanta district
LiLei, year is 16, score is 80.5
Address: HeBei province HengShui city TaoCheng district

友元的关系是单向的而不是双向的。如果声明了类 B 是类 A 的友元类，
不等于类 A 是类 B 的友元类，
类 A 中的成员函数不能访问类 B 中的 private 成员。

友元的关系不能传递。如果类 B 是类 A 的友元类，
类 C 是类 B 的友元类，
不等于类 C 是类 A 的友元类。

除非有必要，一般不建议把整个类声明为友元类，
而只将某些成员函数声明为友元函数，这样更安全一些。
*/
