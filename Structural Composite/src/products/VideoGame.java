package products;

public class VideoGame extends Product {
    public VideoGame(String title, double price)
    {
        super(title, price);
    }
    public double calculatePrice()
    {
        return getPrice();
    }
}
