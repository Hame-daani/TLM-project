
public class Production {

	protected Wing leftWing;
	protected Wing rightWing;

	public Production(String f) {
		String[] temp = f.split("->");
		this.leftWing = new Wing(temp[0]);
		this.rightWing = new Wing(temp[1]);
	}

	public void print() {
		System.out.println(this.leftWing.form + "->" + this.rightWing.form);
	}

	@Override
	public String toString() {

		return this.leftWing.form + "->" + this.rightWing.form;
	}

	public Production remove(char a) {
		Production temp = new Production(this.toString());
		int index = temp.rightWing.variables.indexOf(a);
		temp.rightWing.variables.remove(index);
		temp.rightWing.form = temp.rightWing.form.replace(Character.toString(a), "");
		return temp;
	}
}
