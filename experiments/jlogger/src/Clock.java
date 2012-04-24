/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 1:19:11 PM
 */
public class Clock extends Thread {
	private final Summarizer sum;

	public Clock(Summarizer sum) {
		this.sum = sum;
	}

	public void tic() {
		sum.flush();
	}

	public void run() {
		//for (;;)
		for (int foo = 0; foo < 1; foo++)
		{
			try {
				Thread.sleep(1000);
				//int i = VerStub.random(2);
			} catch (InterruptedException e) {
				return;
			}
			tic();
		}
	}
}
