import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

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

	// get a list of nullables and check if their exist in right wing
	public boolean checkForNull(List<Character> nulls) {
		if (this.rightWing.terminals.size() == 0) {
			Iterator<Character> iter = this.rightWing.variables.iterator();
			while (iter.hasNext()) {
				if (!nulls.contains(iter.next()))
					return false;
			}
			return true;
		}
		return false;
	}

	// get a list of nullables and return their that exist in right wing
	public List<Character> getNulls(List<Character> nullables) {
		List<Character> nulls = new ArrayList<>();
		Iterator<Character> iter = this.rightWing.variables.iterator();
		while (iter.hasNext()) {
			char c = iter.next();
			if (nullables.contains(c))
				nulls.add(c);
		}
		return nulls;
	}
	
}