package pyftpclient_layer;

import pypy.parlib.net.inetworkreader.INetworkReader_72;

import paskma.ftpclient.net.INetworkReader;

/**
 * Internal infrastructure
 * 
 * Connects the generated pypy code to pure Java implementation
 * of networking.
 */
public class CNetworkReader extends INetworkReader_72 {
	private final INetworkReader impl;
	
	public CNetworkReader(INetworkReader impl) {
		this.impl = impl;
	}
	
	public String oreadLine() {
		return impl.readLine();
	}
	
	public int oread() {
		return impl.read();
	}
	
	public String oreadAll() {
		byte[] bytes = impl.readAll();

		if (bytes == null)
			return null;

		// conversion without encoding/decoding		
		char[] chars = new char[bytes.length];
		for (int i = 0; i < bytes.length; i++) {
			chars[i] = (char)bytes[i];
		}
		return new String(chars);
	}
	
	public boolean oclose() {
		return impl.close();
	}
	
}
