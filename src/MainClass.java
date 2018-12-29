import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

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
		
		String fileName = "loader.txt";
		try {
			Scanner loaderScanner = new Scanner(new File(fileName));
			while(loaderScanner.hasNextLine()) {
				input = loaderScanner.nextLine();
				g1.addProductions(input);
			}
			loaderScanner.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		

		g1.removeLanda();
		Iterator<Production> iter = g1.productions.iterator();
		while (iter.hasNext()) {
			System.out.println(iter.next());
		}
		System.out.println("done");
	}

}
