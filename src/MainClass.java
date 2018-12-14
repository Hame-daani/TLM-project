import java.util.ArrayList;
import java.util.List;

public class MainClass {

	public static void main(String[] args) {

		String input = "S";

		List<Character> vars = new ArrayList<>();
		for (char c : input.toCharArray()) {
			vars.add(c);
		}

		char start = vars.get(0);
		input = "ab";

		List<Character> terms = new ArrayList<>();
		for (char c : input.toCharArray()) {
			terms.add(c);
		}
		ContextFree g1 = new ContextFree(vars, terms, start);
		input = "S->aSa";
		g1.addProductions(input);
		input = "S->bSb";
		g1.addProductions(input);
		input = "S->$";
		g1.addProductions(input);
		System.out.println(g1.Is_CFG());
	}

}
