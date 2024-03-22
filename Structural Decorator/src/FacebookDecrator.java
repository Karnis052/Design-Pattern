public class FacebookDecrator extends BaseNotifierDecorator {
    public FacebookDecrator(INotifier wrapped)
    {
        super(wrapped);
    }
    public void send(String msg)
    {
        super.send(msg);
        String fbName = databaseService.getFBNameFromUsername(getUsername());
        System.out.println("Sending " + msg + " on Facebook to " + fbName);
    }
}
