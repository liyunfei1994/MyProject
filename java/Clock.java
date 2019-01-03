import java.util.Scanner;

public class Main1{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		Clock clock = new Clock(in.nextInt(), in.nextInt(), in.nextInt());
		clock.tick();
		System.out.println(clock);
		in.close();
	}
}

class Display{
	private int limit = 0;
	private int value = 0;

	public Display(int limit){
		this.limit = limit;
	}
	public void setValue(int value){
		this.value = value;
	}
	public boolean increase(){
		boolean temp = false;
		value++;
		if (value == limit){
			value = 0;
			temp = true;
		}
		return temp;
	}
	public int getValue(){
		return value;
	}
}

class Clock{
	private Display hour = new Display(24);
	private Display minute = new Display(60);
	private Display second = new Display(60);

	public Clock(int hour, int minute, int second){
		this.hour.setValue(hour);
		this.minute.setValue(minute);
		this.second.setValue(second);
	}
	public String toString(){
		return String.format("%02d:%02d:%02d", hour.getValue(), minute.getValue(), second.getValue());
	}
	public void tick(){
		if (this.second.increase() == true){
			if (this.minute.increase() == true){
				this.hour.increase();
			}
		}
	}

}
12 23 45
12:23:46

12 23 59
12:24:00

