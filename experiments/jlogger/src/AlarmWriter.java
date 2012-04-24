/**
 * User: paskma
 * Date: Nov 11, 2010
 * Time: 1:37:02 PM
 */
public class AlarmWriter extends Thread {
	private final Summarizer sum;

	public AlarmWriter(Summarizer sum) {
		this.sum = sum;
	}

	public void run() {
		for (int i = 0; i < 1; i++) {
			sum.flushAlarm();
		}
	}
}
