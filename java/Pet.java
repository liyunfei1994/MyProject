class Pet{
	private String name;
	private String mastername;

	public Pet(String name, String mastername){
		this.name = name;
		this.mastername = mastername;
	}

	public String getName(){
		return name;
	}
	public String getMasterName(){
		return mastername;
	}

	public void introduce(){
		System.out.println("我的名字是"+name);
		System.out.println("我主人的名字是"+mastername);
	}
}

class RobotPet extends Pet{
	public RobotPet(String name, String mastername){
		super( name, mastername);
	}

	public void introduce(){
		System.out.println("我是机器人。名字是"+getName());
		System.out.println("我的主人是"+getMasterName());
	}
	public void work(int sw){
		switch(sw){
			case 0: System.out.println("打扫");	break;
			case 1: System.out.println("洗衣服");	break;
			case 2: System.out.println("做饭");	break;
		}
	}
}
