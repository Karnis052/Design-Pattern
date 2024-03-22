public class App {
    public static void main(String[] args) throws Exception {
       INotifier notifyAll = new FacebookDecrator(new WhatsAppDecorator(new Notifier("Karnis")));
        notifyAll.send("Hello from all the services");

        System.out.println("==========================================");

        INotifier notifuFbMail = new FacebookDecrator(new Notifier("Karnis"));
        notifuFbMail.send("Hello");
    }
}
