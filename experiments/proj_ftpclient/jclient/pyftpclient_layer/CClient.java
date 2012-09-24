package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_73;
import pypy.Client.__init___80;
import pypy.ftpclient.ftp_file.FtpFile_103;
import pypy.ftpclient.filestream.FileStream_79;

import pypy.test.netimpl.testnetwork.TestNetwork_69;
import pypy.TestNetwork.__init___72;
import pypy.test.server.Server_67;
import pypy.Server.__init___68;

import pypy.test.server_random.RandServer_88;
import pypy.RandServer.__init___90;
import pypy.test.netimpl_random.testnetwork.RandTestNetwork_91;
import pypy.RandTestNetwork.__init___92;

/**
 * The FTP client to be used by an application.
 * 
 * Create, login, download files.
 */
public class CClient {
	private Client_73 impl;
	
	/**
	 * Communication with real world server
	 */
	public static final int NET_WILD = 1;
	/**
	 * Communication with kind buil-in server
	 */
	public static final int NET_TEST = 2;
	/**
	 * Communication with built-in server that fails
	 * to confirm data transfer.
	 */
	public static final int NET_TEST_FAIL = 3;
	/**
	 * Communication with built-in server that respond by
	 * a random code to every command
	 */
	public static final int NET_RAND = 4;
	
	/**
	 * Default constructor for communicating with real FTP server
	 */
	public CClient() {
		init(NET_WILD);
	}
	
	/**
	 * Se NET_* constants.
	 */
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
			__init___90.invoke(server);
			RandTestNetwork_91 commandNet = new RandTestNetwork_91();
			__init___92.invoke(commandNet, server, false);
			RandTestNetwork_91 dataNet = new RandTestNetwork_91();
			__init___92.invoke(dataNet, server, true);
			
			__init___80.invoke(impl, commandNet, dataNet);
		}
	}
	
	/**
	 * Switches the client bug ON/OFF
	 */
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
			FtpFile_103 file = (FtpFile_103)i;
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
