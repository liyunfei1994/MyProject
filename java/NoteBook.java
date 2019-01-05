package notebook;

import java.util.ArrayList;

public class NoteBook {
	private ArrayList<String> notes = new ArrayList<String>();
	public void add(String s) {
		notes.add(s);
	}
	public void add(String s, int location) {
		notes.add(location, s);
	}
	public int getSize() {
		return notes.size();
	}
	public String getNote(int index) {
		return notes.get(index);
	}
	public void removeNote(int index) {
		notes.remove(index);
	}
	public String[] list() {
		String[] a = new String[notes.size()];
		for (int i = 0; i<a.length; i++) {
			a[i] = notes.get(i);
		}
		return a;
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		NoteBook nb = new NoteBook();
		nb.add("first");
		nb.add("second");
		nb.add("lll", 1);
//		System.out.println(nb.getSize());
//		System.out.println(nb.getNote(2));
		String[] k = nb.list();
		for (String s:k) {
			System.out.println(s);
		}
	}

}
