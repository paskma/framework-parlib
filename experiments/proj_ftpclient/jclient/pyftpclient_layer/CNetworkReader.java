package pyftpclient_layer;

import pypy.parlib.net.inetworkreader.INetworkReader_71;

import paskma.ftpclient.net.INetworkReader;

public class CNetworkReader extends INetworkReader_71 {
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
