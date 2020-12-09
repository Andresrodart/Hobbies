import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Client {

    public static void main(String[] args) throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException{
        //get the localhost IP address, if server is running on some other IP, you need to use that
        Socket socket = null;
        ObjectInputStream ois = null;
        //establish socket connection to server
        Date t0 = new Date();
        socket = new Socket("192.168.100.15", 8000);
        //read the server response message
        ois = new ObjectInputStream(socket.getInputStream());
        Date message = (Date) ois.readObject();
        Date t1 =  new Date();
        Date clientTime = new Date (((t1.getTime() - t0.getTime()) / 2) + message.getTime());
        System.out.println("t0: " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(t0));
      	System.out.println("Message: " +  new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(message));
      	System.out.println("t1: " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(t1));
        System.out.println("Client: " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(clientTime));
        //close resources
        ois.close();
      	socket.close();
    }
}