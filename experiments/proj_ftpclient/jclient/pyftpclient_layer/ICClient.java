package pyftpclient_layer;

import java.util.ArrayList;

/**
 * The FTP client to be used by an application.
 * 
 * Create, login, download files.
 * 
 * @see CClient
 */
public interface ICClient {	
	
	/**
	 * Switches the confirmation client bug ON/OFF
	 */
	public void setDataTransferConfirmationBug(boolean value);
	
	/**
	 * Switches the PASV response reading bug ON/OFF
	 */
	public void setPasvResponseReadingBug(boolean value);
	
	public boolean connect(String host, int port);
	
	public boolean isConnected();
	
	public boolean login(String username, String password);
	
	public CFtpFile[] listFiles();
	
	public boolean changeWorkingDirectory(String directory);
	
	public boolean logout();
	
	public byte[] retrieveFile(String filename);
	
	public CFileStream retrieveFileStream(String filename);
	
	public boolean deleteFile(String filename);
}
