class A
{
	public static int i = 10;

	public static void f()
	{
		System.out.printf("Hello World\n");
	}
}

class TestStatic_1
{
	public static void main(String[] args)
	{
		System.out.printf("i = %d\n", A.i);	// i = 10
		A.f(); //Hello World
	}
}
