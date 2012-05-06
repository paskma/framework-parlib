package pyftpclient_layer;

import pypy.ftpclient.filestream.FileStream_79;


public class CFileStream {
	private final FileStream_79 impl;
	
	public CFileStream(FileStream_79 impl) {
		this.impl = impl;
	}

	public int read() {
		return impl.oread();
	}

	public void close() {
		impl.oclose();
	}
}
