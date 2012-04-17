package parlibutil;

public class Trace {
	public static void name() {
		Thread t = Thread.currentThread();
		System.out.println(t.getName() + "-" + t.toString());
	}

	public static void trace() {
		Thread.currentThread().dumpStack();
	}

	public static void main(String[] args)
	{
		name();
		trace();
	}
}
