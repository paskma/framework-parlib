package pyftpclient_layer;

import pypy.ftpclient.ftp_file.FtpFile_103;

/**
 * One item of directory listing.
 * 
 * Returned by CClient
 */
public class CFtpFile {
	private final FtpFile_103 impl;

	public CFtpFile(FtpFile_103 impl) {
		this.impl = impl;
	}

	public String getName() {
		return impl.ogetName();
	}

	public boolean isDirectory() {
		return impl.oisDirectory();
	}

	public String toString() {
		return impl.otoString();
	}
}
