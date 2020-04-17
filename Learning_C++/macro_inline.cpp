/*
	2020年4月17日18:51:47
	内联函数与宏的关系
*/

#include <iostream>

using namespace std;

inline int SQ(int y){return y*y;}

int main(int argc, char const *argv[])
{
	int n, sq;

	cin>>n;
	sq = SQ(n);
	cout<<sq<<endl;

	sq = SQ(n+1);
	cout<<sq<<endl;

	sq = 200/SQ(n+1);
	cout<<sq<<endl;

	return 0;
}
/*
9
81
100
2

使用内联函数来替代宏，可以省去很多带参数的宏的很多问题

内联函数在编译时会将函数调用处用函数体替换，
编译完成后函数就不存在了，
所以在链接时不会引发重复定义错误。
这一点和宏很像，宏在预处理时被展开，
编译时就不存在了。
从这个角度讲，内联函数更像是编译期间的宏。
*/
