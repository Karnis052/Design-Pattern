public class HavingDependency {
    private String currentConditions;
    private Emailer emailer;
    public HavingDependency()
    {
        this.emailer = new Emailer();
    }
    public void setCurrentConditions(String waetherDescription)
    {
        this.currentConditions = waetherDescription;
        if(currentConditions.equals("rainy"))
        {
            emailer.sendEmail("It's rainy");
        }
    }
    
}
