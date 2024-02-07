
import java.util.LinkedList;
import java.util.List;

public class DuckSimulator {
	
	public static void main(String[] args) {
		MallardDuck duck = new MallardDuck();
 
		WildTurkey turkey = new WildTurkey();
		Duck turkeyAdapter = new TurkeyAdapter(turkey);

        List<Duck> ducks = new LinkedList<Duck>();
        ducks.add(duck);
        ducks.add(turkeyAdapter);

        for (Duck d : ducks) {
        	d.quack();
            d.fly();
        }
	}
}