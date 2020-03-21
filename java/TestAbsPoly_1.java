/*
	2020 3 21 21:51:09
	The connection between abstract classes and polymorphism
*/
abstract class A
{
	abstract public void f();
}

class B extends A
{
	public void f()
	{
		System.out.printf("BBBB\n");
	}
}

public class TestAbsPoly_1
{
	public static void main(String[] args)
	{
		// A aa = new A(); error
		B bb = new B();
		bb.f();	//BBBB

		A aa; // ok 
		aa = bb;
		aa.f();	//BBBB
	}
}

-------------
-------------

BBBB
BBBB
