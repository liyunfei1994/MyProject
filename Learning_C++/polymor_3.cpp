/*
    2020年4月25日11:01:36
    构成多态的条件

    下面是构成多态的条件：
        必须存在继承关系；
        继承关系中必须有同名的虚函数，并且它们是覆盖关系（函数原型相同）。
        存在基类的指针，通过该指针调用虚函数。
*/


#include <iostream>
using namespace std;

//基类Base
class Base{
public:
    /*
    在基类 Base 中我们将void func()声明为虚函数，
    这样派生类 Derived 中的void func()就会自动成为虚函数
    */
    virtual void func();
    virtual void func(int);
};
void Base::func(){
    cout<<"void Base::func()"<<endl;
}
void Base::func(int n){
    cout<<"void Base::func(int)"<<endl;
}

//派生类Derived
class Derived: public Base{
public:
    void func();
    void func(char *);
};
void Derived::func(){
    cout<<"void Derived::func()"<<endl;
}
void Derived::func(char *str){
    cout<<"void Derived::func(char *)"<<endl;
}

int main(){

    //p 是基类 Base 的指针，但是指向了派生类 Derived 的对象。
    //让基类指针能够访问派生类的成员函数
    /*
    C++提供多态的目的是：
    可以通过基类指针对所有派生类（包括直接派生和间接派生）的成员变量和成员函数
    进行“全方位”的访问，尤其是成员函数。如果没有多态，我们只能访问成员变量。
    */
    Base *p = new Derived();

    //语句p -> func();调用的是派生类的虚函数，构成了多态。
    p -> func();  //输出void Derived::func()

    //语句p -> func(10);调用的是基类的虚函数，因为派生类中没有函数覆盖它。
    p -> func(10);  //输出void Base::func(int)

    //语句p -> func("http://c.biancheng.net");出现编译错误，
    //因为通过基类的指针只能访问从基类继承过去的成员，不能访问派生类新增的成员。
    // p -> func("http://c.biancheng.net");  //compile error

    return 0;
}
