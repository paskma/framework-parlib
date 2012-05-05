package pyftpclient_layer;

import pypy.ftpclient.filestream.FileStream_78;


public class CFileStream {
	private final FileStream_78 impl;
	
	public CFileStream(FileStream_78 impl) {
		this.impl = impl;
	}

	public int read() {
		return impl.oread();
	}

	public void close() {
		impl.oclose();
	}
}
