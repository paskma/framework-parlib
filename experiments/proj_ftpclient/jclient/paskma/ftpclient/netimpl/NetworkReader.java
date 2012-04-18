package paskma.ftpclient.netimpl;

import paskma.ftpclient.net.INetworkReader;

import java.io.*;
import java.net.Socket;

/**
 * User: paskma
 * Date: Oct 10, 2011
 * Time: 12:48:15 PM
 */
public class NetworkReader implements INetworkReader {
	private Socket socket;
	private BufferedReader reader;
	public NetworkReader(Socket socket) {
		this.socket = socket;
		try {
			this.reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		} catch (IOException e) {
			e.printStackTrace();
			this.reader = null;
		}
	}

	/**
	 * For command connection.
	 */
	public String readLine() {
		if (reader == null)
			return null;

		try {
			return reader.readLine();
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	/**
	 * For data connections, closes the socket.
	 */
	public byte[] readAll() {
		try {
			ByteArrayOutputStream result = new ByteArrayOutputStream();
			InputStream input = socket.getInputStream();
			int c;
			while ((c = input.read()) != -1) {
				result.write((byte)c);
			}

			return result.toByteArray();
		} catch (IOException ex) {
			ex.printStackTrace();
			return null;
		} finally {
			close();
		}
	}

	/**
	 * For multi-threaded data connection.
	 */
	public int read() {
		try {
			return reader.read();
		} catch (IOException e) {
			return CODE_ERR;
		}
	}

	public boolean close() {
		if (socket != null) {
			try {
				socket.close();
				return true;
			} catch (IOException e) {
				return false;
			}
		}
		return false;
	}
}
