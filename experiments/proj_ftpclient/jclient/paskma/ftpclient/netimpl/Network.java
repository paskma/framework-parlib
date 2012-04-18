package paskma.ftpclient.netimpl;

import paskma.ftpclient.net.INetwork;
import paskma.ftpclient.net.INetworkReader;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

/**
 * User: paskma
 * Date: Oct 10, 2011
 * Time: 12:45:10 PM
 */
public class Network implements INetwork {
	private Socket socket;

	public boolean connect(String host, int port) {
		try {
			socket = new Socket(host, port);
			return true;
		} catch (IOException e) {
			e.printStackTrace();
			return false;
		}
	}

	public INetworkReader createNetworkReader() {
		return new NetworkReader(socket);
	}

	public boolean sendMessage(String message) {
		try {
			socket.getOutputStream().write(message.getBytes());
			socket.getOutputStream().flush();
			System.out.println("sent: " + message);
			return true;
		} catch (IOException e) {
			return false;
		}
	}
}
