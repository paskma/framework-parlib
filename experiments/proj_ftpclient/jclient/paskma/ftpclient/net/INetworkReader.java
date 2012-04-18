package paskma.ftpclient.net;

/**
 * User: paskma
 * Date: Oct 10, 2011
 * Time: 12:58:37 PM
 */
public interface INetworkReader {
	public final static int CODE_END = -1;
	public final static int CODE_ERR = -2;

	public String readLine();

	/**
	 * Closes the socket
	 * @return
	 */
	public byte[] readAll();
	public int read();
	public boolean close();
}
