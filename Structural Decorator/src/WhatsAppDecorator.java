public class WhatsAppDecorator extends BaseNotifierDecorator {
    public WhatsAppDecorator(INotifier wrapped)
    {
        super(wrapped);
    }
    public void send(String msg)
    {
        super.send(msg);
        String phoneNbr = databaseService.getPhoneNumberFromUsername(getUsername());
        System.out.println("Sending "+ msg + "by WhatsApp on "+ phoneNbr);
    }
}
