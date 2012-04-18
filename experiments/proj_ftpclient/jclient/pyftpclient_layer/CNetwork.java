package pyftpclient_layer;


import pypy.parlib.net.inetwork.INetwork_65;
import pypy.parlib.net.inetworkreader.INetworkReader_66;
import paskma.ftpclient.netimpl.Network;
import pyftpclient_layer.CNetworkReader;

public class CNetwork extends INetwork_65 {

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
	
	public INetworkReader_66 ocreateNetworkReader() {
		return new CNetworkReader(impl.createNetworkReader());
	}
}
