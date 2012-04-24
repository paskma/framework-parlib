/**
 * User: paskma
 * Date: Oct 25, 2010
 * Time: 12:49:38 PM
 */
public class Database {
	public synchronized void insert(int device, int type, int value) {
		//System.out.println(String.format("INSERT(dev %s,type %s,val %s)", device, type, value));
	}

	public synchronized void insertAlarm() {
		System.out.println("INSERT ALARM");
	}
}
