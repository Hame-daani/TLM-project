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
		input = "abc";

		List<Character> terms = new ArrayList<>();
		for (char c : input.toCharArray()) {
			terms.add(c);
		}
		SimpleGrammar g1 = new SimpleGrammar(vars, terms, start);
		input = "S->aS";
		g1.addProductions(input);
		input = "S->bSaS";
		g1.addProductions(input);
		input = "S->c";
		g1.addProductions(input);

		System.out.println(g1.Is_Simple());
	}

}
