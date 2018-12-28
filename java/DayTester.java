import java.util.Scanner;

class DayTester{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		System.out.println("请输入Day1:");
		System.out.print("年:");		int y = in.nextInt();
		System.out.print("月:");		int m = in.nextInt();
		System.out.print("日:");		int d = in.nextInt();

		Day day1 = new Day(y, m, d);
		System.out.println("day1=" + day1);

		Day day2 = new Day(day1);
		System.out.println("创建了和day1相同日期的day2");
		System.out.println("day2="+day2);

		if (day1.equalTo(day2)){
			System.out.println("day1和day2相等");
		}else{
			System.out.println("day1和day2不相等");
		}

		Day d1 = new Day();
		Day d2 = new Day(2018);
		Day d3 = new Day(2018, 12);
		Day d4 = new Day(2018, 12, 26);

		System.out.println("d1 = " + d1);
		System.out.println("d2 = " + d2);
		System.out.println("d3 = " + d3);
		System.out.println("d4 = " + d4);

		Day[] a = new Day[3];
		for (int i=0; i < a.length; i++){
			a[i] = new Day();
		}

		for (int i=0; i < a.length; i++){
			System.out.println("a["+i+"]=" + a[i]);
		}
	}
}


请输入Day1:
年:2018
月:12
日:23
day1=2018年12月23日(日)
创建了和day1相同日期的day2
day2=2018年12月23日(日)
day1和day2相等
d1 = 0001年01月01日(一)
d2 = 2018年01月01日(一)
d3 = 2018年12月01日(六)
d4 = 2018年12月26日(三)
a[0]=0001年01月01日(一)
a[1]=0001年01月01日(一)
a[2]=0001年01月01日(一)
