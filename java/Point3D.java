import java.util.Random;

public class Point3D{
	private static int counter = 0;
	private int id;
	private int x = 0, y = 0, z = 0;
	static{
		Random rand = new Random();
		counter = rand.nextInt(10) * 100;
	}
	{
		id = ++counter;
	}

	public Point3D(){}
	public Point3D(int x){
		this.x = x;
	}
	public Point3D(int x, int y){
		this.x = x;		this.y = y;
	}
	public Point3D(int x, int y, int z){
		this.x = x; 	this.y = y;		this.z = z;
	}
	public static int getCounter(){
		return counter;
	}
	public int getId(){
		return id;
	}
	public String toString(){
		return "("+x+","+y+","+z+")";
	}

}
