interface IT
{
	void f();
}

class A implements IT
{
	public void f()
	{
		System.out.printf("AAAA\n");
	}

}

class TestInter_1
{
	public static void main(String[] args)
	{
		IT it;

		it = new A();
		it.f();	//AAAA

	}
}

/*
	接口中定义的属性 必须是public static final类型
	接口中定义的方法 必须是public abstract的
	因此这些修饰符可以省略

	接口中定义的属性， 在实现类中不能被更改

	一个类只能实现某个接口，不能继承某个接口
	接口可以继承接口

	不可以new 一个接口对象
	但可以定义一个接口引用类型的变量，并将其指向实现接口的对象
	以此达到多态的目的
*/
