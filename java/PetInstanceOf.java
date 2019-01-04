class PetInstanceOf{
	public static void main(String[] args){
		Pet[] a = {
			new Pet("Kurt","wenchuanyi"),
			new RobotPet("R2D2", "liyunfei"),
			new Pet("DDD", "jiabei"),
		};

		for (int i = 0; i < a.length; i++){
			System.out.println("a["+i+"] ");
			if (a[i] instanceof RobotPet){
				((RobotPet)a[i]).work(0);
			}
			else{
				a[i].introduce();
			}
			
		}
	}
}

类类型的变量除了可以引用该类类型的实例之外
还可以引用上位类的实例和下位类的实例
为了确认变量引用的是哪一个类
可以使用instanceof运算符

a[0]
我的名字是Kurt
我主人的名字是wenchuanyi

a[1]
打扫

a[2]
我的名字是DDD
我主人的名字是jiabei
