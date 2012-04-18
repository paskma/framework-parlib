package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_67;
import pypy.Client.__init___74;
import pypy.ftpclient.ftp_file.FtpFile_82;
import pypy.ftpclient.filestream.FileStream_73;

public class CClient {
	private Client_67 impl;
	
	public CClient() {
		impl = new Client_67();
		__init___74.invoke(impl, new CNetwork(), new CNetwork());
	}
	
	public boolean connect(String host, int port) {
		return impl.oconnect(host, port);
	}
	
	public boolean isConnected() {
		return impl.oisConnected();
	}
	
	public boolean login(String username, String password) {
		return impl.ologin(username, password);
	}
	
	public CFtpFile[] listFiles() {
		ArrayList raw = impl.olistFiles();
		if (raw == null)
			return null;
		
		CFtpFile[] result = new CFtpFile[raw.size()];
		int counter = 0;
		for (Object i : raw) {
			FtpFile_82 file = (FtpFile_82)i;
			result[counter++] = new CFtpFile(file);
		}
		
		return result;
	}
	
	public boolean changeWorkingDirectory(String directory) {
		return impl.ochangeWorkingDirectory(directory);
	}
	
	public boolean logout() {
		return impl.ologout();
	}
	
	public byte[] retrieveFile(String filename) {
		String s = impl.oretrieveFile(filename);
		if (s == null)
			return null;
		// conversion without encoding/decoding
		byte[] result = new byte[s.length()];
		for (int i = 0; i < s.length(); i++) {
			result[i] = (byte)s.charAt(i);
		}
		return result;
	}
	
	public CFileStream retrieveFileStream(String filename) {
		FileStream_73 result = impl.oretrieveFileStream(filename);
		if (result == null)
			return null;
			
		return new CFileStream(result);
	}
	
	public boolean deleteFile(String filename) {
		return impl.odeleteFile(filename);
	}
}
