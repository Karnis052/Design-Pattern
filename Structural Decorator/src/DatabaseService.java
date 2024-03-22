public class DatabaseService {
    public String getMailFromUsername(String username)
    {
        return username + "@Mail";
    }
    public String getPhoneNumberFromUsername(String username)
    {
        return username + "@Phone";
    }
    public String getFBNameFromUsername(String username)
    {
        return username + "@Facebook";
    }
}
