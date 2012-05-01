package paskma.main;

import pyftpclient_layer.CClient;
import pyftpclient_layer.CFtpFile;
import pyftpclient_layer.CFileStream;

import java.io.ByteArrayOutputStream;

/**
 * User: paskma
 * Date: Oct 10, 2011
 * Time: 12:40:19 PM
 */
public class Main {
	private static void p(Object o) {
		System.out.println(o);
	}
	
	public static void main(String[] args) {
		if (args.length == 1 && args[0].equals("--test")) {
			demoTestNetwork();
		} else if (args.length == 1 && args[0].equals("--wild")) {
			demoWild();
		} else {
			p("No task given, try either --test or --wild");
		}
	}
	
	private static void demoTestNetwork() {
		p("TestNetwork demo");
		CClient client = new CClient(true);
		client.connect("ignored", 21);
		client.login("anonymous", "osgiftp@kiv.zcu.cz");
		
		CFtpFile lst[];
		lst = client.listFiles();

		for (CFtpFile i : lst) {
			System.out.println(i);
		}
		
		byte[] contentXX = client.retrieveFile("xx");
		p("XX:'" +  (new String(contentXX)) + "'");
		client.logout();
	}

	private static void demoWild() {
		String host;
		host = "ftp.zcu.cz";
		host = "ftp.gnu.org";
		CClient client = new CClient();
		client.connect(host, 21);
		client.login("anonymous", "osgiftp@kiv.zcu.cz");
		
		CFtpFile lst[];
		lst = client.listFiles();

		for (CFtpFile i : lst) {
			System.out.println(i);
		}
		
		client.changeWorkingDirectory("pub");

		lst = client.listFiles();

		for (CFtpFile i : lst) {
			System.out.println(i);
		}

		byte[] welcome = client.retrieveFile("welcome.msg");
		if (welcome != null)
			System.out.println(new String(welcome));

		CFileStream stream = client.retrieveFileStream("welcome.msg");
		ByteArrayOutputStream buffer = new ByteArrayOutputStream();
		int c;
		while ((c = stream.read()) != -1) {
			buffer.write((byte)c);
			break;
		}
		stream.close();
		System.out.println("From stream:");
		System.out.println(new String(buffer.toByteArray()));


		System.out.println("Still healthy?");
		welcome = client.retrieveFile("welcome.msg");
		
		System.out.println("Desperate delete");
		client.deleteFile("mythical_file.docxxx");
		
		client.logout();
		System.out.println("Done.");
	}
}
