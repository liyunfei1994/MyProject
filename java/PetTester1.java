class PetTester1{
	public static void main(String[] args){
		Pet kurt =new Pet("kurt", "李云飞");
		kurt.introduce();
		System.out.println();

		RobotPet r2d2 = new RobotPet("R2D2", "温钏艺");
		r2d2.introduce();
		System.out.println();

		Pet p = r2d2;
		p.introduce();
		// p.work(1);
    #Pet类型的遥控器可以引用Pet类型的实例，也可以引用RobotPet类型的实例
    #但是不具有RobotPet的work方法按钮
		System.out.println();		
		
		RobotPet d = r2d2;
		d.work(1);
    #只有RobotPet的类类型变量具有work方法按钮
	}
}

我的名字是kurt
我主人的名字是李云飞

我是机器人。名字是R2D2
我的主人是温钏艺

我是机器人。名字是R2D2
我的主人是温钏艺

洗衣服

类类型变量由于派生的关系，可以引用各种类类型的实例，这被称为多态

class PetTester2{
	#方法intro的形参p是Pet类型，该方法只负责对p启动方法introduce
	#形参p除了可以接受Pet类类型的引用之外，还可以接受Pet类的下位类RobotPet类类型的引用
	static void intro(Pet p){
		p.introduce();
	}
  
	public static void main(String[] args){
		Pet[] a = {
			new Pet("Kurt", "李云飞"),
			new RobotPet("R2D2", "温钏艺"),
			new Pet("DDD", "加贝"),
		};

		for (Pet p:a){
			intro(p);
			System.out.println();
		}

	}
}

我的名字是Kurt
我主人的名字是李云飞

我是机器人。名字是R2D2
我的主人是温钏艺

我的名字是DDD
我主人的名字是加贝
