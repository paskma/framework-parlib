package paskma.convert;

import pypy.ftpclient.filestream.FileStream_73;


public class CFileStream {
	private final FileStream_73 impl;
	
	public CFileStream(FileStream_73 impl) {
		this.impl = impl;
	}

	public int read() {
		return impl.oread();
	}

	public void close() {
		impl.oclose();
	}
}
