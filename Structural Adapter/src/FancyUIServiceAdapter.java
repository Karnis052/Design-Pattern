public class FancyUIServiceAdapter implements IMultiRestoApp{
    private final FancyUIService  fancyUIService;
    public FancyUIServiceAdapter()
    {
        fancyUIService = new FancyUIService();
    }
    public void displayMenus(XMLData xmlData)
    {
        JsonData jsonData = convertXmlToJson(xmlData);
        System.out.println("Displaying Fancy Menus using converted JSON data...");
        fancyUIService.displayMenus(jsonData);
    }
    public void displayRecommendation(XMLData xmlData)
    {
        JsonData jsonData = convertXmlToJson(xmlData);
        System.out.println("Displaying Fancy Recommendation using converted JSON data...");
        fancyUIService.displayRecommendation(jsonData);
    }
    private JsonData convertXmlToJson(XMLData xmlData)
    {
        System.out.println("converting XML to Json");
        return new JsonData();
    }
}
