package chap12;

public class MemberTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		类类型实例的数组
//		类似于普通数组的初始化赋值
//		int[] a = new int[] {1,2,3};
		Member[] m = {
				new Member("硚口", 101, 27),
				new SpecialMember("黑木", 102, 31, "会费免费"),
				new SpecialMember("松野", 103, 52, "会费减半"),
		};
//		动态联编中调用的是遥控器当前引用的实例中的方法
//		在运行时确定要调用的方法
		for (Member k:m) {
			k.print();
			System.out.println();
		}
	}
}
