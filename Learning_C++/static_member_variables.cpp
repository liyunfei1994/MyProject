/*
	2020年4月19日13:38:08
	静态成员变量

	对象的内存中包含了成员变量，不同的对象占用不同的内存
	这使得不同对象的成员变量相互独立，
	它们的值不受其他对象的影响。
	例如有两个相同类型的对象 a、b，
	它们都有一个成员变量 m_name，
	那么修改 a.m_name 的值不会影响 b.m_name 的值。

	可是有时候我们希望在多个对象之间共享数据，
	对象 a 改变了某份数据后对象 b 可以检测到。
	共享数据的典型使用场景是计数，
	以前面的 Student 类为例，
	如果我们想知道班级中共有多少名学生，
	就可以设置一份共享的变量，
	每次创建对象时让该变量加 1。

	在C++中，我们可以使用静态成员变量来实现多个对象共享数据的目标。
	静态成员变量是一种特殊的成员变量，
	它被关键字static修饰

*/

// class Student{
// public:
//     Student(char *name, int age, float score);
//     void show();
// public:
//     static int m_total;  //静态成员变量
// private:
//     char *m_name;
//     int m_age;
//     float m_score;
// };


/*
static 成员变量属于类，
不属于某个具体的对象，
即使创建多个对象，
也只为 m_total 分配一份内存，
所有对象使用的都是这份内存中的数据。
当某个对象修改了 m_total，也会影响到其他对象。

static 成员变量必须在类声明的外部初始化
int Student::m_total = 0;

静态成员变量在初始化时不能再加 static，
但必须要有数据类型。
被 private、protected、public 修饰的静态成员变量都可以用这种方式初始化。

static 成员变量既可以通过对象来访问，也可以通过类来访问。

static 成员变量不占用对象的内存，
而是在所有对象之外开辟内存，
即使不创建对象也可以访问。
具体来说，static 成员变量和普通的 static 变量类似，
都在内存分区中的全局数据区分配内存，
*/

//这三种方式是等效的。
//通过类类访问 static 成员变量
// Student::m_total = 10;
// //通过对象来访问 static 成员变量
// Student stu("小明", 15, 92.5f);
// stu.m_total = 20;
// //通过对象指针来访问 static 成员变量
// Student *pstu = new Student("李华", 16, 96);
// pstu -> m_total = 20;

#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
    void show();
private:
    static int m_total;  //静态成员变量
private:
    char *m_name;
    int m_age;
    float m_score;
};

//在类声明的外部，初始化静态成员变量
int Student::m_total = 0;

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){
    m_total++;  //操作静态成员变量
}
void Student::show(){
    cout<<m_name<<" year is "<<m_age<<", score is "<<m_score<<"(Total "<<m_total<<" students)"<<endl;
}

int main(){
    //创建匿名对象
    /*
	使用匿名对象无法回收内存，会导致内存泄露，在中大型程序中不建议使用。
	static 成员变量和普通 static 变量一样，
	都在内存分区中的全局数据区分配内存，到程序结束时才释放。
	这就意味着，static 成员变量不随对象的创建而分配内存，
	也不随对象的销毁而释放内存。
	而普通成员变量在对象创建时分配内存，在对象销毁时释放内存。
    */
    (new Student("XiaoMing", 15, 90)) -> show();
    (new Student("LiLei", 16, 80)) -> show();
    (new Student("ZhangHua", 16, 99)) -> show();
    (new Student("WangKang", 14, 60)) -> show();

    return 0;
}

/*
XiaoMing year is 15, score is 90(Total 1 students)
LiLei year is 16, score is 80(Total 2 students)
ZhangHua year is 16, score is 99(Total 3 students)
WangKang year is 14, score is 60(Total 4 students)
*/
