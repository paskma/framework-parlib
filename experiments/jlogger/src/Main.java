/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 1:22:30 PM
 */
public class Main {
	public static void fool() {

	}

	public static void main(String args[]) {
		fool();
		Database database = new Database();
		Summarizer sum = new Summarizer(database);
		Clock clock = new Clock(sum);
		AlarmWriter alarmWriter = new AlarmWriter(sum);
		Driver driver1 = new Driver(1, sum);
		//Driver driver2 = new Driver(2, sum);

		clock.start();
		alarmWriter.start();
		driver1.start();
		//driver2.start();
	}
}
