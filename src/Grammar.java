import java.util.ArrayList;
import java.util.List;

public class Grammar {

	protected List<Character> variables;
	protected List<Character> terminals;
	protected char startVar;
	protected List<Production> productions;

	public Grammar(List<Character> variables, List<Character> terminals, char startVar) {
		this.variables = variables;
		this.terminals = terminals;
		this.startVar = startVar;
		this.productions = new ArrayList<>();
	}


	public void addProductions(String f) {
		this.productions.add(new Production(f));
	}

}
