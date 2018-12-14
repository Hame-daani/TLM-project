
public class Production {

	protected Wing leftWing;
	protected Wing rightWing;

	public Production(String f) {
		String[] temp = f.split("->");
		this.leftWing = new Wing(temp[0]);
		this.rightWing = new Wing(temp[1]);
	}

	public void print() {
		System.out.println(this.leftWing.form + " -> " + this.rightWing.form);
	}
}
