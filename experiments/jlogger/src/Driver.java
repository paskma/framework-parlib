/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 10:57:25 AM
 */
public class Driver extends Thread {
	private final Summarizer sum;
	private final int device;

	public Driver(int device, Summarizer sum) {
		this.sum = sum;
		this.device = device;
	}

	public void run() {
		//for (;;)
		for (int foo = 0; foo < 1; foo++)
		{
			try {
				//int i = VerStub.random(2);
				Thread.sleep(100);
			} catch (InterruptedException e) {
				return;
			}
			//eventArrived();
			alarmArrived();
		}
	}

	public void eventArrived() {
		Event event = new Event(device, Event.MD, 1);
		sum.handle(event);
	}

	public void alarmArrived() {
		sum.handleAlarm();
	}
}
