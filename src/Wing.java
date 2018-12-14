import java.util.ArrayList;
import java.util.List;

public class Wing {

	protected List<Character> variables;
	protected List<Character> terminals;
	protected String form;

	public Wing(String form) {
		this.variables = new ArrayList<>();
		this.terminals = new ArrayList<>();
		this.form = form;
		for (char c : form.toCharArray()) {
			if (Character.isUpperCase(c))
				this.variables.add(c);
			else {
				this.terminals.add(c);
			}
		}
	}

	public int getVarsNum() {
		return this.variables.size();
	}

	public int getTermsNum() {
		return this.terminals.size();
	}

	public String getForm() {
		return this.form;
	}
}
