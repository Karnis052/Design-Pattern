public class WeatherTracker {
    private String currentConditions;
    private Notifier notifier;
    public WeatherTracker(Notifier notifier)
    {
        this.notifier = notifier;
    }
    public void setCurrentConditions(String weatherDescription)
    {
        this.currentConditions = weatherDescription;
        if(currentConditions.equals("rainy"))
        {
            notifier.alterWeatherConditions(currentConditions);
        }
    }
}
