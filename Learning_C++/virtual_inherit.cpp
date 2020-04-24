/*
	2020年4月24日14:20:03
	虚继承

	为了解决多继承时的命名冲突和冗余数据问题，
	C++ 提出了虚继承，使得在派生类中只保留一份间接基类的成员。

	必须在虚派生的真实需求出现前就已经完成虚派生的操作。
	在上图中，当定义 D 类时才出现了对虚派生的需求，
	但是如果 B 类和 C 类不是从 A 类虚派生得到的，
	那么 D 类还是会保留 A 类的两份成员。
*/

//间接基类A
class A{
protected:
    int m_a;
};

//直接基类B
class B: virtual public A{  //虚继承
protected:
    int m_b;
};

//直接基类C
class C: virtual public A{  //虚继承
protected:
    int m_c;
};

//派生类D
class D: public B, public C{
public:
    void seta(int a){ m_a = a; }  //正确
    void setb(int b){ m_b = b; }  //正确
    void setc(int c){ m_c = c; }  //正确
    void setd(int d){ m_d = d; }  //正确
private:
    int m_d;
};

int main(){
    D d;
    return 0;
}

/*
这段代码使用虚继承重新实现了上图所示的菱形继承，
这样在派生类 D 中就只保留了一份成员变量 m_a，直接访问就不会再有歧义了。

虚继承的目的是让某个类做出声明，承诺愿意共享它的基类。
其中，这个被共享的基类就称为虚基类（Virtual Base Class），
本例中的 A 就是一个虚基类。在这种机制下，
不论虚基类在继承体系中出现了多少次，
在派生类中都只包含一份虚基类的成员。


*/
