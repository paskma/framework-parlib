package pyftpclient_layer;

import pypy.ftpclient.filestream.FileStream_80;

/**
 * File stream for downloading large files.
 *
 * Returned by CClient.
 */
public class CFileStream {
	private final FileStream_80 impl;
	
	public CFileStream(FileStream_80 impl) {
		this.impl = impl;
	}

	public int read() {
		return impl.oread();
	}

	public void close() {
		impl.oclose();
	}
}
