/*
	2020年4月19日10:58:40
	成员对象和封闭类

	一个类的成员变量 如果是另一个类的对象
	就称之为 成员对象，
	包含成员对象的类 就叫作 封闭类
*/

#include <iostream>
using namespace std;

//轮胎类
class Tyre{
public:
    Tyre(int radius, int width);
    void show() const;
private:
    int m_radius;  //半径
    int m_width;  //宽度
};

Tyre::Tyre(int radius, int width) : m_radius(radius), m_width(width){ }
void Tyre::show() const {
    cout << "radius: " << this->m_radius << "inch" << endl;
    cout << "width: " << this->m_width << "mm" << endl;
}

//引擎类
class Engine{
public:
    Engine(float displacement = 2.0);
    void show() const;
private:
    float m_displacement;
};

Engine::Engine(float displacement) : m_displacement(displacement) {}
void Engine::show() const {
    cout << "displacement:" << this->m_displacement << "L" << endl;
}

//汽车类
class Car{
public:
    Car(int price, int radius, int width);
    void show() const;
private:
    int m_price;  //价格
    Tyre m_tyre;
    Engine m_engine;
};

//借助封闭类构造函数的初始化列表。
Car::Car(int price, int radius, int width): m_price(price), m_tyre(radius, width)/*指明m_tyre对象的初始化方式*/{ };
void Car::show() const {
    cout << "Price:" << this->m_price << "$" << endl;
    this->m_tyre.show();
    this->m_engine.show();
}

int main()
{
	//编译器需要知道 car 对象中的 m_tyre 和 m_engine 成员对象该如何初始化。
	/*
	m_tyre 应以 radius 和 width 作为参数调用 Tyre(int radius, int width) 构造函数初始化。
	但是这里并没有说明 m_engine 该如何处理。在这种情况下，
	编译器就认为 m_engine 应该用 Engine 类的无参构造函数初始化。
	而 Engine 类确实有一个无参构造函数（因为设置了默认参数），
	因此，整个 car 对象的初始化问题就都解决了。
	*/
    Car car(200000, 19, 245);
    car.show();
    return 0;
}

----------------
Price:200000$
radius: 19inch
width: 245mm
displacement:2L
