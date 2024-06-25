public class BeefBurgerRestuarant extends Restuarant {
    @Override
    public Burger createBurger()
    {
        System.out.println("Creating Beef Burger...");
        return new BeefBurger();
    }
}
