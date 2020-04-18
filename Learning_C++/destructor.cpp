/*
	2020年4月18日19:31:21
	析构函数

	创建对象时系统会自动调用构造函数进行初始化工作，
	同样，销毁对象时系统也会自动调用一个函数来进行清理工作，
	例如释放分配的内存、关闭打开的文件等，
	这个函数就是析构函数。

	析构函数（Destructor）也是一种特殊的成员函数，
	没有返回值，不需要程序员显式调用（程序员也没法显式调用），
	而是在销毁对象时自动执行。
	构造函数的名字和类名相同，
	而析构函数的名字是在类名前面加一个~符号。

	析构函数没有参数，不能被重载，
	因此一个类只能有一个析构函数。
	如果用户没有定义，
	编译器会自动生成一个默认的析构函数。
*/

#include <iostream>
using namespace std;

class VLA{
public:
    VLA(int len);  //构造函数
    //~VLA()就是 VLA 类的析构函数，
    //它的唯一作用就是在删除对象(76 line)后释放已经分配的内存。
    ~VLA();  //析构函数
public:
    void input();  //从控制台输入数组元素
    void show();  //显示数组元素
private:
    int *at(int i);  //获取第i个元素的指针
private:
    const int m_len;  //数组长度
    int *m_arr; //数组指针
    int *m_p;  //指向数组第i个元素的指针
};

VLA::VLA(int len): m_len(len){  //使用初始化列表来给const成员变量 m_len 赋值
    if(len > 0){ m_arr = new int[len];  /*分配内存*/ }
    else{ m_arr = NULL; }
}
VLA::~VLA(){
    delete[] m_arr;  //释放内存
}
void VLA::input(){
    for(int i=0; m_p=at(i); i++){ cin>>*at(i); }
}
void VLA::show(){
    for(int i=0; m_p=at(i); i++){
        if(i == m_len - 1){ cout<<*at(i)<<endl; }
        else{ cout<<*at(i)<<", "; }
    }
}
int * VLA::at(int i){
    if(!m_arr || i<0 || i>=m_len){ return NULL; }
    else{ return m_arr + i; }
}

int main(){
    //创建一个有n个元素的数组（对象）
    int n;
    cout<<"Input array length: ";
    cin>>n;
    VLA *parr = new VLA(n);
    //输入数组元素
    cout<<"Input "<<n<<" numbers: ";
    parr -> input();
    //输出数组元素
    cout<<"Elements: ";
    parr -> show();
    //删除数组（对象）
    delete parr;

    return 0;
}
/*
用 new 分配内存时会调用构造函数，
用 delete 释放内存时会调用析构函数。
构造函数和析构函数对于类来说是不可或缺的，
所以在C++中我们非常鼓励使用 new 和 delete。

Input array length: 5
Input 5 numbers: 99 23 45 10 100
Elements: 99, 23, 45, 10, 100
*/
