import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
/**
 * Dummy firebase client. reads input from command line,
 * sends it to the python script
 * */

public class Main {

    public static void main(String[] args) {
        Socket echoSocket;
        DataOutputStream dout;
        BufferedReader din;
        String fromServ;
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();
        while (!input.equalsIgnoreCase("exit")) {
            try {
                echoSocket = new Socket("localhost", 2004);
                dout = new DataOutputStream(echoSocket.getOutputStream());
                din = new BufferedReader(new InputStreamReader(echoSocket.getInputStream(), "UTF-8"));
                dout.writeUTF(input);
                dout.flush();
                fromServ = din.readLine().trim();
                System.out.println(fromServ);
                input = in.nextLine();
                echoSocket.close();
                dout.close();
                din.close();
            } catch (UnknownHostException e) {
                System.err.println("Don't know about host.");
            } catch (IOException e) {
                e.printStackTrace();
                System.err.println("Couldn't get I/O");
            }
        }
    }
}
