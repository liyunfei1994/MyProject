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

class C extends B
{
	public void f()
	{
		System.out.printf("CCCC\n");
	}
}

public class TestPoly_2
{
	public static void g(A aa)
	{
		aa.f();
	}

	public static void main(String[] args)
	{
		A aa = new A();
		B bb = new B();
		C cc = new C();

		g(aa);
		g(bb);
		g(cc);
	}
}

---------------
---------------

AAAA
BBBB
CCCC
