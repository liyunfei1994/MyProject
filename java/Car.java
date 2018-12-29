public class  Car {
	private String name;
	private int width;
	private int height;
	private int length;
	private double x;
	private double y;
	private double fuel;
	private Day purchaseDay;

	public Car(String name, int width, int height, int length, double fuel,
		Day purchaseDay){
		this.name = name;	this.width =width;	this.height = height;
		this.length = length;	this.fuel =fuel;	x = y = 0.0;
		this.purchaseDay = new Day(purchaseDay);
	}

	public double getX(){return x;}
	public double getY(){return y;}
	public double getFuel(){return fuel;}
	public Day getPurchaseDay(){
		return new Day(purchaseDay);
	}

	public void putSpec(){
		System.out.println("名称:"+name);
		System.out.println("宽度:"+width);
		System.out.println("高度:"+height);
		System.out.println("长度:"+length);		
	}

	public boolean move(double dx, double dy){
		double dist = Math.sqrt(dx*dx+dy*dy);
		if(dist>fuel){
			return false;
		}else{
			fuel -= dist;
			x += dx;
			y += dy;
			return true;
		}
	}
	
}
