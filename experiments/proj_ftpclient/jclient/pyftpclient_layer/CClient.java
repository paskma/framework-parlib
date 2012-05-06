package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_73;
import pypy.Client.__init___80;
import pypy.ftpclient.ftp_file.FtpFile_105;
import pypy.ftpclient.filestream.FileStream_79;

import pypy.test.netimpl.testnetwork.TestNetwork_69;
import pypy.TestNetwork.__init___72;
import pypy.test.server.Server_67;
import pypy.Server.__init___68;

import pypy.test.server_random.RandServer_88;
import pypy.RandServer.__init___89;
import pypy.test.netimpl_random.testnetwork.RandTestNetwork_90;
import pypy.RandTestNetwork.__init___91;

public class CClient {
	private Client_73 impl;
	
	public static final int NET_WILD = 1;
	public static final int NET_TEST = 2;
	public static final int NET_TEST_FAIL = 3;
	public static final int NET_RAND = 4;
	
	public CClient() {
		init(NET_WILD);
	}
	
	public CClient(int networkType) {
		init(networkType);
	}
	
	private void init(int networkType) {
		impl = new Client_73();
		if (networkType == NET_TEST || networkType == NET_TEST_FAIL) {
			Server_67 server = new Server_67();
			__init___68.invoke(server);
			if (networkType == NET_TEST_FAIL){
				server.osetExperimentErrorDataTransferConfirmation(true);
			}
			
			TestNetwork_69 commandNet = new TestNetwork_69();
			__init___72.invoke(commandNet, server, false);
			TestNetwork_69 dataNet = new TestNetwork_69();
			__init___72.invoke(dataNet, server, true);

			
			__init___80.invoke(impl, commandNet, dataNet);
		} else if (networkType == NET_WILD) {
			__init___80.invoke(impl, new CNetwork(), new CNetwork());
		} else if (networkType == NET_RAND) {
			RandServer_88 server = new RandServer_88();
			__init___89.invoke(server);
			RandTestNetwork_90 commandNet = new RandTestNetwork_90();
			__init___91.invoke(commandNet, server, false);
			RandTestNetwork_90 dataNet = new RandTestNetwork_90();
			__init___91.invoke(dataNet, server, true);
			
			__init___80.invoke(impl, commandNet, dataNet);
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
			FtpFile_105 file = (FtpFile_105)i;
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
		FileStream_79 result = impl.oretrieveFileStream(filename);
		if (result == null)
			return null;
			
		return new CFileStream(result);
	}
	
	public boolean deleteFile(String filename) {
		return impl.odeleteFile(filename);
	}
}
