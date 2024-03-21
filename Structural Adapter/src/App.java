public class App {
    public static void main(String[] args) throws Exception {
        XMLData xmlData = new XMLData();
        IMultiRestoApp multiRestoApp = new MultiRestoApp();
        multiRestoApp.displayMenus(xmlData);
        multiRestoApp.displayRecommendation(xmlData);

        System.out.println("==========================================");
        IMultiRestoApp adapter = new FancyUIServiceAdapter();
        adapter.displayMenus(xmlData);
        adapter.displayRecommendation(xmlData);
    }
}
    