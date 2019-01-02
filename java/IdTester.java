class Id{
	static int counter = 0;

	private int id;
	public Id(){
		id = ++counter;
	}
	public int getId(){
		return id;
	}

}

public class IdTester{
	public static void main(String[] args){
		Id a = new Id();
		Id b = new Id();

		System.out.println("a的标识编号为："+ a.getId());
		System.out.println("b的标识编号为："+ b.getId());

		System.out.println("Id.counter = "+ Id.counter);
		System.out.println("a.counter = "+ a.counter);
		System.out.println("b.counter = "+ b.counter);
	}
}

a的标识编号为：1
b的标识编号为：2
Id.counter = 2
a.counter = 2
b.counter = 2
