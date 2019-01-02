import java.util.Scanner;

class DayTester{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);

		int y, m, d;
		System.out.println("公历年份:");
		y = in.nextInt();
		System.out.println("该年"+(Day.isLeap(y)? "是闰年":"不是闰年"));

		System.out.println("请输入日期：");
		System.out.print("年:");		y = in.nextInt();
		System.out.print("月:");		m = in.nextInt();
		System.out.print("日:");		d = in.nextInt();
		Day a = new Day(y, m, d);
		System.out.println(a.getYear()+"年"+(a.isLeap()? "是闰年":"不是闰年"));
	}
}

公历年份:
2019
该年不是闰年
请输入日期：
年:2004
月:12
日:23
2004年是闰年
