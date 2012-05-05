package pyftpclient_layer;

import pypy.ftpclient.ftp_file.FtpFile_90;

public class CFtpFile {
	private final FtpFile_90 impl;

	public CFtpFile(FtpFile_90 impl) {
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
