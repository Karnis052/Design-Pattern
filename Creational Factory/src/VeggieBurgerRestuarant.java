public class VeggieBurgerRestuarant extends Restuarant {
    @Override
    public Burger createBurger()
    {
        System.out.println("Creating Veggie Burger...");
        return new VeggieBurger();
    }
}
