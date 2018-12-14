import java.util.List;

public class ContextFree extends Grammar {

	public ContextFree(List<Character> variables, List<Character> terminals, char startVar) {
		super(variables, terminals, startVar);
	}

	public boolean IS_CFG() {
		for (Production p : this.productions) {
			if (p.leftWing.getVarsNum() != 1 || p.leftWing.getTermsNum() != 0) {
				p.print();
				return false;
			}
		}
		return true;
	}
}
