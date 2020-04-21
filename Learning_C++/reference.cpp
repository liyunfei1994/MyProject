/*
	2020年4月21日20:21:23
	引用

	引用（Reference）是 C++ 相对于C语言的又一个扩充。
	引用可以看做是数据的一个别名，
	通过这个别名和原来的名字都能够找到这份数据。
	引用类似于 Windows 中的快捷方式，
	一个可执行程序可以有多个快捷方式，
	通过这些快捷方式和可执行程序本身都能够运行程序；
	引用还类似于人的绰号（笔名），
	使用绰号（笔名）和本名都能表示一个人。

	引用的定义方式类似于指针，只是用&取代了*，语法格式为：
	type &name = data;
*/

// #include <iostream>
// using namespace std;

// int main() {
//     int a = 99;
//     int &r = a;
/*
		引用在定义时需要添加&，在使用时不能添加&，使用时添加&表示取地址。
*/
//     r = 47;
//     cout << a << ", " << r << endl;

//     return 0;
// }

//C++引用作为函数参数
/*
在定义或声明函数时，我们可以将函数的形参指定为引用的形式，
这样在调用函数时就会将实参和形参绑定在一起，
让它们都指代同一份数据。
如此一来，如果在函数体中修改了形参的数据，
那么实参的数据也会被修改，
从而拥有“在函数内部影响函数外部数据”的效果。
*/

#include <iostream>
using namespace std;

void swap1(int a, int b);
void swap2(int *p1, int *p2);
void swap3(int &r1, int &r2);


int main() {
    int num1, num2;
    cout << "Input two integers: ";
    cin >> num1 >> num2;
    cout<<"use real number"<<endl;
    swap1(num1, num2);
    cout << num1 << " " << num2 << endl;

    cout << "Input two integers: ";
    cin >> num1 >> num2;
    cout<<"use pointer"<<endl;
    swap2(&num1, &num2);
    cout << num1 << " " << num2 << endl;

    cout << "Input two integers: ";
    cin >> num1 >> num2;
    cout<<"use reference"<<endl;
    swap3(num1, num2);
    cout << num1 << " " << num2 << endl;

    int a = 99;
    int &r = a;
    cout<<a<<", "<<r<<endl;
    cout<<&a<<", "<<&r<<endl;
    /*
	99, 99
	变量是要占用内存的，虽然我们称 r 为变量，
	但是通过&r获取到的却不是 r 的地址，
	而是 a 的地址，这会让我们觉得 r 这个变量不占用独立的内存，
	它和 a 指代的是同一份内存。
	0x64ff1c, 0x64ff1c
    */


    return 0;
}

//直接传递参数内容
void swap1(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

//传递指针
void swap2(int *p1, int *p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

//按引用传参
/*
我鼓励读者大量使用引用，
它一般可以代替指针（当然指针在C++中也不可或缺），
C++ 标准库也是这样做的。
*/
void swap3(int &r1, int &r2) {
    int temp = r1;
    r1 = r2;
    r2 = temp;
}
