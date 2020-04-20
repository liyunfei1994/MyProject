/*
	2020年4月20日16:39:01
	将其他类的成员函数 声明为友元类
*/

#include <iostream>
using namespace std;

//对 Address 类进行了提前声明，是因为在 Address 类定义之前、
//在 Student 类中使用到了它，如果不提前声明，编译器会报错，
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

//定义Address类
class Address{
private:
    char *m_province;  //省份
    char *m_city;  //城市
    char *m_district;  //区（市区）
public:
    Address(char *province, char *city, char *district);
    //将Student类中的成员函数show()声明为友元函数
    //friend 函数不仅可以是全局函数（非成员函数），还可以是另外一个类的成员函数。
    //可以使得其他类中的成员函数以及全局范围内的函数访问当前类的 private 成员。
    //将 Student 类的成员函数 show() 声明为 Address 类的友元函数，
    //由此，show() 就可以访问 Address 类的 private 成员变量了。
    //在当前类以外定义的、不属于当前类的函数也可以在类中声明，
    //但要在前面加 friend 关键字，这样就构成了友元函数
    friend void Student::show(Address *addr);
};

//实现Student类
Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){ }
void Student::show(Address *addr){
    cout<<m_name<<", year is "<<m_age<<", score is "<<m_score<<endl;
    cout<<"Address: "<<addr->m_province<<" province "<<addr->m_city<<" City "<<addr->m_district<<" district"<<endl;
}

//实现Address类
Address::Address(char *province, char *city, char *district){
    m_province = province;
    m_city = city;
    m_district = district;
}

int main(){
    Student stu("XiaoMing", 16, 95.5f);
    Address addr("ShanXi", "Xian", "YanTa");
    stu.show(&addr);
   
    Student *pstu = new Student("LiLei", 16, 80.5);
    Address *paddr = new Address("HeBei", "HengShui", "TaoCheng");
    pstu -> show(paddr);

    return 0;
}

/*
XiaoMing, year is 16, score is 95.5
Address: ShanXi province Xian City YanTa district
LiLei, year is 16, score is 80.5
Address: HeBei province HengShui City TaoCheng district
*/
