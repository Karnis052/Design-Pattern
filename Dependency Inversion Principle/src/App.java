public class App{
    public static void main(String[] arg) throws Exception{
        // HavingDependency weatherTracker = new HavingDependency();
        // weatherTracker.setCurrentConditions("rainy");
        Notifier emailNotifier = new Email();
        WeatherTracker weatherTracker = new WeatherTracker(emailNotifier);
        weatherTracker.setCurrentConditions("rainy");

        Notifier SMSNotifier = new SMS();
        WeatherTracker weatherTracker2 = new WeatherTracker(SMSNotifier);
        weatherTracker2.setCurrentConditions("rainy");
    }
}