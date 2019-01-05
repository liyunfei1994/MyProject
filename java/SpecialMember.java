package chap12;

public class SpecialMember extends Member {
	private String privilege;
	public SpecialMember(String name, int no, int age, String privilege) {
//		super()表达式用于调用超类的构造函数
//		将“将形参name， no，age接受到的值赋给字段name， no， age”的处理委托给超类的构造函数
//		子类的构造函数只是对新添加的字段进行赋值
//		只可以在构造函数的开头调用super();
		super(name, no, age);
		this.privilege = privilege;
	}
	
//	注解是编译器也可以读懂的注释
//	方法重写的时候使用的是@Override注解，在方法声明的前面加上
//	告诉编译器，接下来的方法是重写上位类的方法，而不是本类中新添加的方法
	@Override public void print() {
//		超类的成员可以通过super.成员名进行访问
		super.print();
		System.out.println("优惠："+privilege);
	}
	
	
	
}
