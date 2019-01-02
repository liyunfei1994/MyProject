class AccountTester{
	public static void main(String[] args){
		Account liyunfei = new Account("李云飞", "026882", 1000);
		Account wenchuanyi = new Account("温钏艺", "123456", 2000);

		System.out.println("李云飞的账户：");
		System.out.println("账户名："+liyunfei.getName());
		System.out.println("账号："+liyunfei.getNo());
		System.out.println("余额："+liyunfei.getBalance());
		System.out.println("标识编号："+liyunfei.getId());

		System.out.println("温钏艺的账户：");
		System.out.println("账户名："+wenchuanyi.getName());
		System.out.println("账号："+wenchuanyi.getNo());
		System.out.println("余额："+wenchuanyi.getBalance());
		System.out.println("标识编号："+wenchuanyi.getId());
	}
}

李云飞的账户：
账户名：李云飞
账号：026882
余额：1000
标识编号：1

温钏艺的账户：
账户名：温钏艺
账号：123456
余额：2000
标识编号：2
