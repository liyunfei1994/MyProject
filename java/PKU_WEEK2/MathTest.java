package mathtest;

public class MathTest {
	private int number;
	private int sum;
	
	public void setSum() {
		sum += number*number*number;
//		return sum;
	}
	public void setNumber(int number) {
		this.number = number;
//		return number;
	}
	public int getNumber() {
		return number;
	}
	public int getSum() {
		return sum;
	}
	

}
