import java.util.ArrayList;

/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 10:22:19 AM
 */
public class Summarizer {
	private final ArrayList<SumField> fields; // avoid invokeinterface
	private final Database database;
	private int filled = 0; // 2 == false
	private int alarm = 0;

	public Summarizer(Database database) {
		this.fields = new ArrayList<SumField>();
		this.database = database;
	}

	public synchronized void handle(Event event) {
		filled = 1;
		int handleProbe = filled;
		/*boolean found = false;
		for (int index = 0; index < fields.size(); index++) {
			SumField i = fields.get(index);

			if (i.device == event.getDevice() && i.type == event.getType()) {
				//i.value += event.getValue();
				found = true;
				break;
			}
		}

		if (!found) {
			SumField field = new SumField(event.getDevice(), event.getType());
			field.value = event.getValue();
			fields.add(field);
		}*/
	}

	public synchronized void handleAlarm() {
		alarm++;
		notify();
	}

	private void pass() {
	}

	private void clear() {
	}

	private void push() {
		//clear(); // bug
		database.insert(0, 0, 0);
		clear();
	}

	public synchronized void flush() {
		int flushProbe = filled;

		if (filled == 1) {
			push();
		} else {
			pass();
		}
		/*
		for (int i = 0; i < fields.size(); i++) {
			SumField field = fields.get(i);
			database.insert(field.device, field.type, field.value);
		}
		fields.clear();
		*/
	}

	public synchronized void flushAlarm() {
		//System.out.println("fa start");
		while (alarm == 0) {
			try {
				//System.out.println("fa wait");
				wait();
			} catch (InterruptedException e) {
			}
		}

		//System.out.println("fa call insert");
		database.insertAlarm();
		alarm--;
	}
}
