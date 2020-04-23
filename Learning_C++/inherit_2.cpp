/*
	2020年4月23日17:49:20
	C++ 三种继承方式

	C++继承的一般语法为：
	class 派生类名:［继承方式］ 基类名{
	    派生类新增加的成员
	};

	类成员的访问权限由高到低依次为 public --> protected --> private，
	public 成员可以通过对象来访问，private 成员不能通过对象访问。

	protected 成员和 private 成员类似，也不能通过对象访问。
	但是当存在继承关系时，protected 和 private 就不一样了：
	基类中的 protected 成员可以在派生类中使用，
	而基类中的 private 成员不能在派生类中使用

	public、protected、private 指定继承方式：

	不同的继承方式会影响基类成员在派生类中的访问权限。

	1) public继承方式
	基类中所有 public 成员在派生类中为 public 属性；
	基类中所有 protected 成员在派生类中为 protected 属性；
	基类中所有 private 成员在派生类中不能使用。

	2) protected继承方式
	基类中的所有 public 成员在派生类中为 protected 属性；
	基类中的所有 protected 成员在派生类中为 protected 属性；
	基类中的所有 private 成员在派生类中不能使用。

	3) private继承方式
	基类中的所有 public 成员在派生类中均为 private 属性；
	基类中的所有 protected 成员在派生类中均为 private 属性；
	基类中的所有 private 成员在派生类中不能使用。
	
	1) 基类成员在派生类中的访问权限不得高于继承方式中指定的权限。

	也就是说，
	继承方式中的 public、protected、private 是用来指明基类成员在派生类中的最高访问权限的。

	2) 不管继承方式如何，
		基类中的 private 成员在派生类中始终不能使用（不能在派生类的成员函数中访问或调用）。

	由于 private 和 protected 继承方式会改变基类成员在派生类中的访问权限，
	导致继承关系复杂，所以实际开发中我们一般使用 public。
*/

#include<iostream>
using namespace std;

//基类People
class People{
public:
    void setname(char *name);
    void setage(int age);
    void sethobby(char *hobby);
    char *gethobby();
protected:
	//基类中的 protected 成员可以在派生类中使用，
    char *m_name;
    int m_age;
private:
    char *m_hobby;
};
void People::setname(char *name){ m_name = name; }
void People::setage(int age){ m_age = age; }
void People::sethobby(char *hobby){ m_hobby = hobby; }
char *People::gethobby(){ return m_hobby; }

//派生类Student
class Student: public People{
public:
    void setscore(float score);
protected:
    float m_score;
};
void Student::setscore(float score){ m_score = score; }

//派生类Pupil
class Pupil: public Student{
public:
    void setranking(int ranking);
    void display();
private:
    int m_ranking;
};
void Pupil::setranking(int ranking){ m_ranking = ranking; }
void Pupil::display(){
    cout<<m_name<<", age is "<<m_age<<", score is "<<m_score<<", ranking is "<<m_ranking<<", he likes "<<gethobby()<<"."<<endl;
}

int main(){
    Pupil pup;
    pup.setname("XiaoMing");
    pup.setage(15);
    pup.setscore(92.5f);
    pup.setranking(4);
    pup.sethobby("Basketball");
    pup.display();

    return 0;
}
/*
XiaoMing, age is 15, score is 92.5, ranking is 4, he likes Basketball.
*/
