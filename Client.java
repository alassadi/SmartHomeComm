import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
    public static void main(String[] args) {
        Socket echoSocket;
        DataOutputStream dout;
        BufferedReader din;
        String fromServ;

        try {

            echoSocket = new Socket("localhost", 2004);
            dout=new DataOutputStream(echoSocket.getOutputStream());
             din=new BufferedReader(new InputStreamReader(echoSocket.getInputStream(), "UTF-8"));


            dout.writeUTF("Hello Python! This is your message");
            dout.flush();

             fromServ = din.readLine().trim();

            System.out.println(fromServ);


            echoSocket.close();
            dout.close();
            din.close();


        } catch(UnknownHostException e){
            System.err.println("Don't know about host.");

        } catch(IOException e){
            e.printStackTrace();
            System.err.println("Couldn't get I/O");

        }
    }
    }

