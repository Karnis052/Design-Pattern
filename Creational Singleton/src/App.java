public class App {
    public static void main(String[] args)  {
        Singleton instanceSingleton =  Singleton.getInstance("It is singleton instance");
        instanceSingleton.printValue();
    }
}
