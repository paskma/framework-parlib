package pyftpclient_layer;


import pypy.parlib.net.inetwork.INetwork_70;
import pypy.parlib.net.inetworkreader.INetworkReader_71;
import paskma.ftpclient.netimpl.Network;
import pyftpclient_layer.CNetworkReader;

public class CNetwork extends INetwork_70 {

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
	
	public INetworkReader_71 ocreateNetworkReader() {
		return new CNetworkReader(impl.createNetworkReader());
	}
}
