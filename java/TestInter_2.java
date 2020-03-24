interface IT1
{
	void f();

	void g();
}

/*
	如果一个类 只实现了接口的部分方法，则该类必须声明为抽象类
*/

abstract class A implements IT1 
{
	public void f()
	{
		System.out.printf("AAAA\n");
	}
}

public class TestInter_2
{
	public static void main(String[] args)
	{
		System.out.printf("Hello World!\n");
	}
}
