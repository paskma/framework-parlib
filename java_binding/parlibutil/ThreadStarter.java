package parlibutil;

public class ThreadStarter extends Thread {
	
	public ThreadStarter() {
		//setDaemon(true);
	}
	
	public void oRUN() {
		// will be overriden
		// System.out.println("ThreadStarter::oRUN()");
	}

	public void run() {
		// System.out.println("ThreadStarter::run()");
		// Trace.name();
		oRUN();
	}
}
