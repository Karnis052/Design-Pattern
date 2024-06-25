public class SMS implements Notifier {
    public void alterWeatherConditions(String msg)
    {
        System.out.println("Set alert by sms " + msg);
    }
}
