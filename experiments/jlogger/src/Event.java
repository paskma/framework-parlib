/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 10:22:57 AM
 */
public class Event {
	public static final int MD = 1;
	public static final int DI = 2;

	private final int type;
	private final int value;
	private final int device;

	public Event(int device, int type, int value) {
		this.device = device;
		this.type = type;
		this.value = value;
	}

	public int getType() {
		return type;
	}

	public int getValue() {
		return value;
	}

	public int getDevice() {
		return device;
	}
}
