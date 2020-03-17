/*
  2020年3月17日11:16:49
  本程序证明：A类的多个对象 共用一个static属性
*/
class A
{
	public static int i = 10;

	public void show()
	{
		System.out.printf("i = %d\n", i);
	}
}

class TestStatic
{
	public static void main(String[] args)
	{
		A aa1 = new A();
		A aa2 = new A();

		aa1.i = 999;
		aa2.show();	//i=999
	}
}
