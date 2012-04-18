package paskma.ftpclient.net;

/**
 * User: paskma
 * Date: Oct 10, 2011
 * Time: 12:44:01 PM
 */
public interface INetwork {
	public boolean connect(String host, int port);
	public boolean sendMessage(String message);
	public INetworkReader createNetworkReader();
}
