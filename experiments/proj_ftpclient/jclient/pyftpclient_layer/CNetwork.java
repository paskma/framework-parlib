package pyftpclient_layer;


import pypy.parlib.net.inetwork.INetwork_78;
import pypy.parlib.net.inetworkreader.INetworkReader_79;
import paskma.ftpclient.netimpl.Network;
import pyftpclient_layer.CNetworkReader;

/**
 * Internal infrastructure.
 * 
 * Connects the generated pypy code to pure Java implementation
 * of networking.
 */
public class CNetwork extends INetwork_78 {

	private Network impl;
	
	public CNetwork() {
		impl = new Network();
	}
	

	public boolean oconnect(String host, int port) {
		return impl.connect(host, port);
	}
	
	public boolean osendMessage(String message) {
		return impl.sendMessage(message);
	}
	
	public INetworkReader_79 ocreateNetworkReader() {
		return new CNetworkReader(impl.createNetworkReader());
	}
}
