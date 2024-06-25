public class Email implements Notifier{
    public void alterWeatherConditions(String msg)
    {
        System.out.println("Set alert by email "+ msg);
    }
}
