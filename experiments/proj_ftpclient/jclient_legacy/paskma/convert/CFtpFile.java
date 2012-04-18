package paskma.convert;

import pypy.ftpclient.ftp_file.FtpFile_82;

public class CFtpFile {
	private final FtpFile_82 impl;

	public CFtpFile(FtpFile_82 impl) {
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
