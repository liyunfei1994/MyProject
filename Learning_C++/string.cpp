/*
	2020年4月20日20:33:14
	string

	C++ 大大增强了对字符串的支持，除了可以使用C风格的字符串，
	还可以使用内置的 string 类。
	string 类处理起字符串来会方便很多，
	完全可以代替C语言中的字符数组或字符串指针。

	string 是 C++ 中常用的一个类，它非常重要，

	与C风格的字符串不同，string 的结尾没有结束标志'\0'
*/

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	// string s = "liyunfei";
	// //当我们需要知道字符串长度时，可以调用 string 类提供的 length() 函数
	// int len = s.length();

	// cout<<len<<endl; //8

	// string a;
	// cin>>s;
	// cout<<s<<endl;

	//liyunfei wenchuanyi
	// liyunfei
	//我们输入了两个由空格隔开的网址，但是只输出了一个，
	//这是因为输入运算符>>默认会忽略空格，遇到空格就认为输入结束

	string s = "1234567890";
	for (int i=0, len=s.length(); i<len; ++i)
	{
		cout<<s[i]<<" ";
	}
	cout<<endl;
	s[5] = '5';
	cout<<s<<endl;

	//字符串的拼接
	/*
	用+来拼接字符串时，运算符的两边可以都是 string 字符串，
	也可以是一个 string 字符串和一个C风格的字符串，
	还可以是一个 string 字符串和一个字符数组，
	或者是一个 string 字符串和一个单独的字符。
	*/
	// string s1 = "first ";
	// string s2 = "second ";
	// char *s3 = "third";
	// char s4[] = "fourth";
	// char ch = '@';

	// string s5 = s1 + s2;
	// string s6 = s1 + s3;
	// string s7 = s1 + s4;
	// string s8 = s1 + ch;

	// cout<<s5<<endl<<s6<<endl<<s7<<endl<<s8<<endl;
	/*
	first second
	first third
	first fourth
	first @
	*/

	//字符串的插入
	// string s1, s2, s3;
 //    s1 = s2 = "1234567890";
 //    s3 = "aaa";
 //    s1.insert(5, s3);
 //    cout<< s1 <<endl;
 //    s2.insert(5, "bbb");
 //    cout<< s2 <<endl;

	//字符串的删除
	// string s1, s2, s3;
 //    s1 = s2 = s3 = "1234567890";
 //    s2.erase(5);
 //    s3.erase(5, 3);
 //    cout<< s1 <<endl;
 //    cout<< s2 <<endl;
 //    cout<< s3 <<endl;

    /*
	1234567890
	12345
	1234590
    */

    //提取子字符串
    string s1 = "first second third";
    string s2;
    s2 = s1.substr(6, 6);
    cout<< s1 <<endl;
    cout<< s2 <<endl;

    /*
	first second third
	second	
    */

	return 0;
}
