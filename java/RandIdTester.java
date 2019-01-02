import java.util.Random;

class RandId{
	private static int counter;
	private int id;

	static{
		Random rand = new Random();
		counter = rand.nextInt(10) * 100;
	}

	public RandId(){
		id = ++counter;
	}
	public int getId(){
		return id;
	}

}
public class RandIdTester{
	public static void main(String[] args){
		RandId a = new RandId();
		RandId b = new RandId();
		RandId c = new RandId();

		System.out.println("a的标识编号为："+a.getId());
		System.out.println("b的标识编号为："+b.getId());
		System.out.println("c的标识编号为："+c.getId());
	}
}


a的标识编号为：201
b的标识编号为：202
c的标识编号为：203
