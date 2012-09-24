package pyftpclient_layer;

import java.util.ArrayList;

import pypy.ftpclient.client.Client_74;
import pypy.Client.__init___81;
import pypy.ftpclient.ftp_file.FtpFile_104;
import pypy.ftpclient.filestream.FileStream_80;

import pypy.test.netimpl.testnetwork.TestNetwork_70;
import pypy.TestNetwork.__init___73;
import pypy.test.server.Server_68;
import pypy.Server.__init___69;

import pypy.test.server_random.RandServer_89;
import pypy.RandServer.__init___92;
import pypy.test.netimpl_random.testnetwork.RandTestNetwork_93;
import pypy.RandTestNetwork.__init___94;
import pypy.test.server_random.RandServerConfig_90;
import pypy.RandServerConfig.__init___100;

/**
 * The FTP client to be used by an application.
 * 
 * Create, login, download files.
 */
public class CClient {
	private Client_74 impl;
	
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
		impl = new Client_74();
		if (networkType == NET_TEST || networkType == NET_TEST_FAIL) {
			Server_68 server = new Server_68();
			__init___69.invoke(server);
			if (networkType == NET_TEST_FAIL){
				server.osetExperimentErrorDataTransferConfirmation(true);
			}
			
			TestNetwork_70 commandNet = new TestNetwork_70();
			__init___73.invoke(commandNet, server, false);
			TestNetwork_70 dataNet = new TestNetwork_70();
			__init___73.invoke(dataNet, server, true);

			
			__init___81.invoke(impl, commandNet, dataNet);
		} else if (networkType == NET_WILD) {
			__init___81.invoke(impl, new CNetwork(), new CNetwork());
		} else if (networkType == NET_CODE_RAND || networkType == NET_LINE_CUT_RAND) {
			RandServerConfig_90 config = null;
			
			if (networkType == NET_LINE_CUT_RAND) {
				config = new RandServerConfig_90();
				__init___100.invoke(config);
				config.osetSERVER_LEVEL(0);
				config.osetREADLINE_LEVEL(2);
			}
			
			RandServer_89 server = new RandServer_89();
			__init___92.invoke(server, config);
			RandTestNetwork_93 commandNet = new RandTestNetwork_93();
			__init___94.invoke(commandNet, server, false, config);
			RandTestNetwork_93 dataNet = new RandTestNetwork_93();
			__init___94.invoke(dataNet, server, true, config);
			
			__init___81.invoke(impl, commandNet, dataNet);
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
	
	public CFtpFile[] listFiles() {
		ArrayList raw = impl.olistFiles();
		if (raw == null)
			return null;
		
		CFtpFile[] result = new CFtpFile[raw.size()];
		int counter = 0;
		for (Object i : raw) {
			FtpFile_104 file = (FtpFile_104)i;
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
		FileStream_80 result = impl.oretrieveFileStream(filename);
		if (result == null)
			return null;
			
		return new CFileStream(result);
	}
	
	public boolean deleteFile(String filename) {
		return impl.odeleteFile(filename);
	}
}
