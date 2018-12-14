import java.util.List;

public class SimpleGrammar extends ContextFree {

	public SimpleGrammar(List<Character> variables, List<Character> terminals, char startVar) {
		super(variables, terminals, startVar);
	}

	public boolean Is_Simple() {
		if (this.IS_CFG())
			if (this.occurrenceCheck() && this.productsCheck())
				return true;
		return false;
	}

	public boolean occurrenceCheck() {
		boolean occurs[][] = new boolean[this.variables.size()][this.terminals.size()];
		int varIndex, terIndex;

		for (Production p : this.productions) {
			varIndex = this.variables.indexOf(p.leftWing.form.charAt(0));
			terIndex = this.terminals.indexOf(p.rightWing.form.charAt(0));
			if (occurs[varIndex][terIndex]) {
				p.print();
				return false;
			} else
				occurs[varIndex][terIndex] = true;
		}

		return true;
	}

	public boolean productsCheck() {
		for (Production p : this.productions) {
			if (Character.isLowerCase(p.rightWing.form.charAt(0))) {
				for (char c : p.rightWing.form.substring(1, p.rightWing.form.length()).toCharArray()) {
					if (Character.isLowerCase(c)) {
						p.print();
						return false;
					}
				}
			} else {
				p.print();
				return false;
			}
		}

		return true;
	}

}
