class A
{
	public void f()
	{
		System.out.printf("AAAA\n");
	}
}

class B extends A
{
	public void f()
	{
		System.out.printf("BBBB\n");
	}
}

class TestPoly_1
{
	public static void main(String[] args)
	{
		A aa = new A();
		B bb = new B();

		aa.f(); //AAAA
		bb.f(); //BBBB

		aa = bb;
		aa.f(); //BBBB
	}
}

-----------------------
-----------------------

AAAA
BBBB
BBBB
