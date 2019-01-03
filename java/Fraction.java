import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);
		Fraction a = new Fraction(in.nextInt(), in.nextInt());
		Fraction b = new Fraction(in.nextInt(),in.nextInt());
		a.print();
		b.print();
		a.plus(b).print();
		a.multiply(b).plus(new Fraction(5,6)).print();
		a.print();
		b.print();
		in.close();

	}


}

class Fraction{
	private int molecular, denominator;
	public Fraction(int a, int b){
		this.molecular = a;
		this.denominator = b;
	}

	public double toDouble(){
		return molecular*1.0/denominator;
	}

	public Fraction plus(Fraction r){
		Fraction m = new Fraction(0, 1);
		m.denominator = r.denominator * denominator;
		m.molecular = molecular*r.denominator+denominator*r.molecular;
		return m;
	}
	public Fraction multiply(Fraction r){
		Fraction m = new Fraction(0,1);
		m.denominator = r.denominator*denominator;
		m.molecular = molecular*r.molecular;
		return m;
	}

	void print(){
		int r, x = denominator, y = molecular;
		while(y!=0){
			r = x%y;
			x = y;
			y = r;
		}
		molecular /= x;
		denominator /= x;
		if(molecular == denominator){
			System.out.println(molecular/denominator);
		}else{
			System.out.println(molecular+"/"+denominator);
		}
		return;
	}
}
