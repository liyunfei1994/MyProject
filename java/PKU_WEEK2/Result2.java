package mathtest;
import java.math.BigDecimal;
import java.util.Scanner;
public class Result {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("基础部分验证");
		Scanner in = new Scanner(System.in);
		System.out.print("请输入第一个正整数:");
		int a = in.nextInt();
		System.out.print("请输入最后一个正整数:");
		int b = in.nextInt();
		System.out.print("请输入需要验证的正整数:");
		int n = in.nextInt();
		
		MathTest test = new MathTest();
		for (int i = a; i <= b; i++) {
			test.setNumber(i);
			test.setSum();
		}
		if(test.getSum() == n*n*n) {
			System.out.println("等式成立");
		}
		else {
			System.out.println("等式不成立");
		}
		
		System.out.println("拓展部分，寻找更多蛮多以上要求的式子");
//		1^3+2^3+3^3+...+n^3 = [n(n+1)/2]^2
//		即（1^3+2^3+3^3+……+y^3）-（1^3+2^3+3^3+……+(x-1)^3）
//		表示(x^3+(x+1)^3+(x+2)^3+……+y^3)
//		如果[y*(y+1)/2]^2-[(x-1)*x/2]^2
//		开三次方的结果为一个正整数则等式成立
		System.out.println("寻找[k~j]内满足要求的正整数，k=<y<=j");
		System.out.print("请输入一个正整数k:");
		int k = in.nextInt();
		System.out.print("请输入一个正整数j:");
		int j = in.nextInt();
		
		double m;
		for (double y = k; y <= j; y++) {
			 for(double x = 1; x < y; x++) {
				 m = (y*(y+1)/2)*(y*(y+1)/2)-((x-1)*x/2)*((x-1)*x/2);
			 
				 double c = Math.pow(m,  1.0/3);
				 BigDecimal d = new BigDecimal(c);
				 c = d.setScale(7,BigDecimal.ROUND_HALF_UP).doubleValue();
				 if (c == (int)c) {
					 System.out.println("第一个数是"+ (int)x +"最后一个整数是"+(int)y);
					 System.out.println("找到的数:"+(int)c);
			 }
		}
		}
		in.close();

	}

}

基础部分验证
请输入第一个正整数:3
请输入最后一个正整数:5
请输入需要验证的正整数:6
等式成立
拓展部分，寻找更多蛮多以上要求的式子
寻找[k~j]内满足要求的正整数，k=<y<=j
请输入一个正整数k:1
请输入一个正整数j:15
第一个数是3最后一个整数是5
找到的数:6
第一个数是11最后一个整数是14
找到的数:20
