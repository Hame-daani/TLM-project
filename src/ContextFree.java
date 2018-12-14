import java.util.ArrayList;
import java.util.Iterator;
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

	// public Chomsky toChomsky() {
	//
	// }

	public void removeLanda() {
		List<Character> nullables = new ArrayList<>();
		// if a->$ add a to nulls
		for (Production p : this.productions) {
			if (p.rightWing.terminals.contains('$')) {
				nullables.add(p.leftWing.variables.get(0));
			}
		}
		// if b->a add b to nulls
		for (Production p : this.productions) {
			if (checkRightForNull(p, nullables)) {
				nullables.add(p.leftWing.variables.get(0));
			}
		}
		List<Production> newProducts = new ArrayList<>();
		// add to new list
		for (Production p : this.productions) {
			if (!p.rightWing.terminals.contains('$')) {
				newProducts.add(p);
				List<Character> nulls = getNulls(p, nullables);
				if (nulls.size() > 0) {
					Iterator<Character> iter = nulls.iterator();
					while (iter.hasNext()) {
						char a = iter.next();
						newProducts.add(p.remove(a));
						Iterator<Character> iter2 = nulls.listIterator(nulls.indexOf(a) + 1);
						while (iter2.hasNext()) {
							char b = iter2.next();
							newProducts.add(p.remove(a).remove(b));
						}
					}
				}
			}
		}
		// all done
		this.productions = newProducts;
	}

	public boolean checkRightForNull(Production p, List<Character> nulls) {
		if (p.rightWing.terminals.size() == 0) {
			Iterator<Character> iter = p.rightWing.variables.iterator();
			while (iter.hasNext()) {
				if (!nulls.contains(iter.next()))
					return false;
			}
			return true;
		}
		return false;
	}

	public List<Character> getNulls(Production p, List<Character> nullables) {
		List<Character> nulls = new ArrayList<>();
		Iterator<Character> iter = p.rightWing.variables.iterator();
		while (iter.hasNext()) {
			char c = iter.next();
			if (nullables.contains(c))
				nulls.add(c);
		}
		return nulls;
	}

}
