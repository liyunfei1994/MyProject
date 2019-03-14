package mathtest;
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

	}

}

基础部分验证
请输入第一个正整数:6
请输入最后一个正整数:69
请输入需要验证的正整数:180
等式成立

基础部分验证
请输入第一个正整数:3
请输入最后一个正整数:5
请输入需要验证的正整数:6
等式成立
