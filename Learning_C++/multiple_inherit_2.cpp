/*
	2020年4月24日14:05:27
	菱形继承会出现的问题

	类 A 派生出类 B 和类 C，类 D 继承自类 B 和类 C，
	这个时候类 A 中的成员变量和成员函数继承到类 D 中变成了两份，
	一份来自 A-->B-->D 这条路径，
	另一份来自 A-->C-->D 这条路径。
*/

//间接基类A
class A{
protected:
    int m_a;
};

//直接基类B
class B: public A{
protected:
    int m_b;
};

//直接基类C
class C: public A{
protected:
    int m_c;
};

//派生类D
class D: public B, public C{
public:
    // void seta(int a){ m_a = a; }  //error 命名冲突  reference to `m_a' is ambiguous
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
