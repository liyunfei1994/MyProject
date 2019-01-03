class A{
	private int a;
	A(){a = 50;}
	int getA(){
		return a;
	}

}

class B extends A{

}

public class Default{
	public static void main(String[] args){
		B x = new B();
		System.out.println("x.getA() = "+ x.getA());
	}
}

x.getA() = 50
