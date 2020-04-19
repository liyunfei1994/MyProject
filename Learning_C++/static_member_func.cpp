/*
	2020年4月19日18:47:28
	静态成员函数

	在类中，static 除了可以声明静态成员变量，还可以声明静态成员函数。
	普通成员函数可以访问所有成员（包括成员变量和成员函数），
	静态成员函数只能访问静态成员。

	编译器在编译一个普通成员函数时，
	会隐式地增加一个形参 this，
	并把当前对象的地址赋值给 this，
	所以普通成员函数只能在创建对象后通过对象来调用，
	因为它需要当前对象的地址。
	而静态成员函数可以通过类来直接调用，
	编译器不会为它增加形参 this，
	它不需要当前对象的地址，
	所以不管有没有创建对象，都可以调用静态成员函数。

	普通成员变量占用对象的内存，静态成员函数没有 this 指针，
	不知道指向哪个对象，无法访问对象的成员变量，
	也就是说静态成员函数不能访问普通成员变量，只能访问静态成员变量。

	静态成员函数与普通成员函数的根本区别在于：
	普通成员函数有 this 指针，可以访问类中的任意成员；
	而静态成员函数没有 this 指针，
	只能访问静态成员（包括静态成员变量和静态成员函数）。

*/

#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
    void show();
public:  //声明静态成员函数, 在C++中，静态成员函数的主要目的是访问静态成员。
    static int getTotal();
    static float getPoints();
private:
    static int m_total;  //总人数
    static float m_points;  //总成绩
private:
    char *m_name;
    int m_age;
    float m_score;
};

int Student::m_total = 0;
float Student::m_points = 0.0;

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){
    m_total++;
    m_points += score;
}
void Student::show(){
    cout<<m_name<<" year is "<<m_age<<", score is "<<m_score<<endl;
}
//定义静态成员函数
//和静态成员变量类似，静态成员函数在声明时要加 static，在定义时不能加 static
int Student::getTotal(){
    return m_total;
}
float Student::getPoints(){
    return m_points;
}

int main(){
    (new Student("XiaoMing", 15, 90.6)) -> show();
    (new Student("LiLei", 16, 80.5)) -> show();
    (new Student("ZhangHua", 16, 99.0)) -> show();
    (new Student("WangKang", 14, 60.8)) -> show();

    int total = Student::getTotal();
    float points = Student::getPoints();
    cout<<"Total of "<<total<<" students, total score is "<<points<<", the average score is "<<points/total<<endl;

    return 0;
}

/*
XiaoMing year is 15, score is 90.6
LiLei year is 16, score is 80.5
ZhangHua year is 16, score is 99
WangKang year is 14, score is 60.8
Total of 4 students, total score is 330.9, the average score is 82.725
*/
