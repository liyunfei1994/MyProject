import java.util.Scanner;

class CarTester3{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);

		System.out.println("请输入汽车的数据:");
		System.out.print("名称:");	String name = in.next();
		System.out.print("宽度:");	int width = in.nextInt();
		System.out.print("高度:");	int height = in.nextInt();
		System.out.print("长度:");	int length = in.nextInt();

		System.out.print("燃料:");	double fuel = in.nextDouble();
		System.out.print("购买年份:");	int y = in.nextInt();
		System.out.print("购买月份:");	int m = in.nextInt();
		System.out.print("购买日期:");	int d = in.nextInt();

		Car car2 = new Car(name, width, height, length, fuel, new Day(y, m, d));

		car2.putSpec();
		System.out.println("购买日期为:"+car2.getPurchaseDay());

	}
}


请输入汽车的数据:
名称:劳斯莱斯
宽度:1800
高度:1900
长度:1850
燃料:100
购买年份:2018
购买月份:12
购买日期:28
名称:劳斯莱斯
宽度:1800
高度:1900
长度:1850
购买日期为:2018年12月28日(五)
