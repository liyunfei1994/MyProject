class Human
{
	private String name;
	private int age;

	public Human()
	{

	}

	public Human(String name, int age)
	{
		this.name = name;
		this.age = age;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public void setAge(int age)
	{
		this.age = age;
	}

	public String getInfo()
	{
		String strInfo = name + ": " + age;
		return strInfo;
	}
}

class Student extends Human
{
	public String school;

	public Student()
	{

	}

	public Student(String name, int age, String school)
	{
		super(name, age); //super init
		this.school = school;
	}

	public void setSchool(String school)
	{
		this.school = school;
	}

	public String getInfo()
	{
		String strInfo = super.getInfo() + " "+ school; 
		//call the normal method of the superclass
		return strInfo;
	}
}

class TestStudent
{
	public static void main(String[] args)
	{
		Student st1 = new Student("Michael Lee", 26, "Prime School");
		System.out.printf("%s\n", st1.getInfo());
	}
}

-------------------
-------------------

Michael Lee: 26 Prime School
