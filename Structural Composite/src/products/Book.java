package products;

public class Book extends Product {
    public Book(String title, double price)
    {
        super(title, price);
    }
    public double calculatePrice()
    {
        return getPrice();
    }
}
