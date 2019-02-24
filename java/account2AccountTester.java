package chap6;

class Account{
//	加上private的字段，访问属性就变成了私有访问
//	私有访问的字段对类的外部是隐藏的
//	因此，类AccountTester中的main方法中无法访问该字段
	private String name;
	private String no;
	private long balance;
	
	Account (String n, String num, long z){
//		赋值的目标不是a.name或者b.name,而是单纯的name
//		构造函数知道自身的实例是哪一个
		name = n;
		no = num;
		balance = z;
	}
//	声明中未加static的方法是实例方法
//	每个实例都有自己专有的方法
//	在实例方法中，不使用a.name或者a.balance,只使用单纯的name和balance
//	访问其所属的实例中的该字段
//	此外，由于实例方法也在类Account的内部，可以访问私有字段
	String getname() {
		return name;
	}
	String getNo(){
		return no;
	}
	long getBalance() {
		return balance;
	}
	void deposit(long k) {
		balance += k;
	}
	void withdraw(long k) {
		balance -= k;
	}
	
	
}

public class AccountTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Account a = new Account("liyunfei","abcd",1000);
		Account b = new Account("wenchuanyi", "oopp", 2000);
		
		System.out.println(a.getname()+"的余额为：" + a.getBalance());
		System.out.println(b.getname()+"的余额为：" + b.getBalance());
		
		a.deposit(100);
		b.withdraw(200);
		
		System.out.println(a.getname()+"的余额为：" + a.getBalance());
		System.out.println(b.getname()+"的余额为：" + b.getBalance());

	}

}
