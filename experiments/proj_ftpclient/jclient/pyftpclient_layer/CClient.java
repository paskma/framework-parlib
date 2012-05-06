package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_72;
import pypy.Client.__init___79;
import pypy.ftpclient.ftp_file.FtpFile_90;
import pypy.ftpclient.filestream.FileStream_78;

import pypy.test.netimpl.testnetwork.TestNetwork_68;
import pypy.TestNetwork.__init___71;
import pypy.test.server.Server_66;
import pypy.Server.__init___67;

public class CClient {
	private Client_72 impl;
	
	public static final int NET_WILD = 1;
	public static final int NET_TEST = 2;
	public static final int NET_TEST_FAIL = 3;
	
	public CClient() {
		init(NET_WILD);
	}
	
	public CClient(int networkType) {
		init(networkType);
	}
	
	private void init(int networkType) {
		impl = new Client_72();
		if (networkType == NET_TEST || networkType == NET_TEST_FAIL) {
			Server_66 server = new Server_66();
			__init___67.invoke(server);
			if (networkType == NET_TEST_FAIL){
				server.osetExperimentErrorDataTransferConfirmation(true);
			}
			
			TestNetwork_68 commandNet = new TestNetwork_68();
			__init___71.invoke(commandNet, server, false);
			TestNetwork_68 dataNet = new TestNetwork_68();
			__init___71.invoke(dataNet, server, true);

			
			__init___79.invoke(impl, commandNet, dataNet);
		} else if (networkType == NET_WILD) {
			__init___79.invoke(impl, new CNetwork(), new CNetwork());
		}
	}
	
	public void setDataTransferConfirmationBug(boolean value) {
		impl.osetDataTransferConfirmationBug(value);
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
			FtpFile_90 file = (FtpFile_90)i;
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
		FileStream_78 result = impl.oretrieveFileStream(filename);
		if (result == null)
			return null;
			
		return new CFileStream(result);
	}
	
	public boolean deleteFile(String filename) {
		return impl.odeleteFile(filename);
	}
}
