package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_81;
import pypy.Client.__init___88;
import pypy.ftpclient.ftp_file.FtpFile_100;
import pypy.ftpclient.filestream.FileStream_87;

import pypy.test.netimpl.testnetwork.TestNetwork_77;
import pypy.TestNetwork.__init___80;
import pypy.test.server.Server_75;
import pypy.Server.__init___76;

import pypy.test.server_random.RandServer_104;
import pypy.RandServer.__init___105;
import pypy.test.netimpl_random.testnetwork.RandTestNetwork_106;
import pypy.RandTestNetwork.__init___107;
import pypy.test.server_random.RandServerConfig_102;
import pypy.RandServerConfig.__init___103;

/**
 * The FTP client to be used by an application.
 * 
 * Create, login, download files.
 */
public class CClient implements ICClient {
	private Client_81 impl;
	
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
	public static final int NET_CODE_RAND = 4;
	/**
	 * Built-in server randomly cuts every response.
	 */
	public static final int NET_LINE_CUT_RAND = 5;
	
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
		impl = new Client_81();
		if (networkType == NET_TEST || networkType == NET_TEST_FAIL) {
			Server_75 server = new Server_75();
			__init___76.invoke(server);
			if (networkType == NET_TEST_FAIL){
				server.osetExperimentErrorDataTransferConfirmation(true);
			}
			
			TestNetwork_77 commandNet = new TestNetwork_77();
			__init___80.invoke(commandNet, server, false);
			TestNetwork_77 dataNet = new TestNetwork_77();
			__init___80.invoke(dataNet, server, true);

			
			__init___88.invoke(impl, commandNet, dataNet);
		} else if (networkType == NET_WILD) {
			__init___88.invoke(impl, new CNetwork(), new CNetwork());
		} else if (networkType == NET_CODE_RAND || networkType == NET_LINE_CUT_RAND) {
			RandServerConfig_102 config = null;
			
			if (networkType == NET_LINE_CUT_RAND) {
				config = new RandServerConfig_102();
				__init___103.invoke(config);
				config.osetSERVER_LEVEL(0);
				config.osetREADLINE_LEVEL(2);
			}
			
			RandServer_104 server = new RandServer_104();
			__init___105.invoke(server, config);
			RandTestNetwork_106 commandNet = new RandTestNetwork_106();
			__init___107.invoke(commandNet, server, false, config);
			RandTestNetwork_106 dataNet = new RandTestNetwork_106();
			__init___107.invoke(dataNet, server, true, config);
			
			__init___88.invoke(impl, commandNet, dataNet);
		}
	}
	
	/**
	 * Switches the confirmation client bug ON/OFF
	 */
	public void setDataTransferConfirmationBug(boolean value) {
		impl.osetDataTransferConfirmationBug(value);
	}
	
	/**
	 * Switches the PASV response reading bug ON/OFF
	 */
	public void setPasvResponseReadingBug(boolean value) {
		impl.osetPasvResponseReadingBug(value);
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
	
	public boolean isLogged() {
		return impl.oisLogged();
	}
	
	public CFtpFile[] listFiles() {
		ArrayList raw = impl.olistFiles();
		if (raw == null)
			return null;
		
		CFtpFile[] result = new CFtpFile[raw.size()];
		int counter = 0;
		for (Object i : raw) {
			FtpFile_100 file = (FtpFile_100)i;
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
		FileStream_87 result = impl.oretrieveFileStream(filename);
		if (result == null)
			return null;
			
		return new CFileStream(result);
	}
	
	public boolean deleteFile(String filename) {
		return impl.odeleteFile(filename);
	}
}
