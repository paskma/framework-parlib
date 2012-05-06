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
		if (args.length != 1) {
			p("No task given. Try one of:");
			p("  --test, --wild, --fail, --fail-cbug, --rand1000, --rand-cbug1000");
			return;
		}
		
		String arg = args[0];
		
		if (arg.equals("--test")) {
			demoTestNetwork();
		} else if (arg.equals("--wild")) {
			demoWild();
		} else if (arg.equals("--fail")) {
			demoFail(false);
		} else if (arg.equals("--fail-cbug")) {
			demoFail(true);
		} else if (arg.equals("--rand")) {
			demoRand(false);
		} else if (arg.equals("--rand-cbug")) {
			demoRand(true);
		} else if (arg.equals("--rand1000")) {
			demoRand(false, 1000);
		} else if (arg.equals("--rand-cbug1000")) {
			demoRand(true, 1000);
		} else {
			p("Option not recognized: " + arg);
		}
	}
	
	private static void demoFail(boolean clientDataConfirmationBug) {
		if (clientDataConfirmationBug)
			p("C:Server fails, client raises exception due to a bug");
		else
			p("C:Server fails, client handles that gracefully");
			
		CClient client = new CClient(CClient.NET_TEST_FAIL);
		client.setDataTransferConfirmationBug(clientDataConfirmationBug);
		client.connect("ignored", 21);
		client.login("anonymous", "osgiftp@kiv.zcu.cz");
		
		byte[] f = client.retrieveFile("xx");
		if (f != null)
			p("C:File is:\n"+ new String(f));
		else
			p("C:File transfer failed.");

		p("C:##Second shot...");
		
		f = client.retrieveFile("xx");
		if (f != null)
			p("C:File(2) is:\n"+ new String(f));
		else
			p("C:File(2) transfer failed.");
		
		client.logout();
		
	}
	
	private static void demoRand(boolean clientDataConfirmationBug, int loops) {
		int i = 0;
		try {
			for (i = 0; i < loops; i++) {
				demoRand(clientDataConfirmationBug);
				//exception will break the loop
			}
			p("All loops performed " + loops);
		} catch (Throwable ex) {
			ex.printStackTrace();
			p("Exception found in loop " + i);
		}
	}
	
	
	private static void demoRand(boolean clientDataConfirmationBug) {
		if (clientDataConfirmationBug)
			p("C:Server with random behavior, client might raises exception due to a bug");
		else
			p("C:Server with random behavior, client handles that gracefully");
			
		CClient client = new CClient(CClient.NET_RAND);
		client.setDataTransferConfirmationBug(clientDataConfirmationBug);

		boolean suc = client.connect("ignored", 21);
		if (!suc) {
			p("C:Can not connect, end.");
			return;
		}
		suc = client.login("anonymous", "osgiftp@kiv.zcu.cz");
		if (!suc) {
			p("C:Can not log in, end.");
			return;
		}
		
		byte[] f = client.retrieveFile("xx");
		if (f != null)
			p("C:File is:\n"+ new String(f));
		else
			p("C:File transfer failed.");

		p("C:##Second shot...");
		
		f = client.retrieveFile("xx");
		if (f != null)
			p("C:File(2) is:\n"+ new String(f));
		else
			p("C:File(2) transfer failed.");
		
		suc = client.logout();
		if (!suc) {
			p("C:Can not logout.");
			return;
		}
	}
	
	private static void demoTestNetwork() {
		p("TestNetwork demo");
		CClient client = new CClient(CClient.NET_TEST);
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
