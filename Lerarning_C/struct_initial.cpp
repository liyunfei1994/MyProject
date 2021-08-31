/*
构造函数初始化结构体

// 1.构造函数内赋值
struct studentInfo{
    int id;
    char gender;
    // 参数对结构体内部变量赋值
    studentInfo(int _id, char _gender){
        // 赋值
        id = _id;
        gender = _gender;
    }
}
// 2.使用初始化列表
struct studentInfo{
    int id;
    char gender;
    // 参数对结构体内部变量赋值
    studentInfo(int _id, char _gender): id(_id), gender(_gender){}
}

*/
#include <iostream>

using namespace std;

struct Point {
    int x, y;
    Point() {} // 不经初始化定义pt[10]
    Point(int _x, int _y) : x(_x), y(_y) {/* 用于x和y的初始化 */ }
}pt[10];

int main() {
    int num = 0;
    for (int i = 1; i <= 3; ++i)
        for (int j = 1; j <= 3; ++j)
            pt[num++] = Point(i, j);
    for (int i = 0; i < num; ++i)
        cout << pt[i].x << ',' << pt[i].y << endl;
    return 0;
}

/*
1,1
1,2
1,3
2,1
2,2
2,3
3,1
3,2
3,3
*/
