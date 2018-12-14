import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class MainClass {

	public static void main(String[] args) {

		String input = "SABCD";

		List<Character> vars = new ArrayList<>();
		for (char c : input.toCharArray()) {
			vars.add(c);
		}

		char start = vars.get(0);
		input = "abcd";

		List<Character> terms = new ArrayList<>();
		for (char c : input.toCharArray()) {
			terms.add(c);
		}
		ContextFree g1 = new ContextFree(vars, terms, start);
		input = "S->ABaC";
		g1.addProductions(input);
		input = "A->BC";
		g1.addProductions(input);
		input = "B->b";
		g1.addProductions(input);
		input = "B->$";
		g1.addProductions(input);
		input = "C->D";
		g1.addProductions(input);
		input = "C->$";
		g1.addProductions(input);
		input = "D->d";
		g1.addProductions(input);

		g1.removeLanda();
		Iterator<Production> iter = g1.productions.iterator();
		while (iter.hasNext()) {
			System.out.println(iter.next());
		}
		System.out.println("done");
	}

}
