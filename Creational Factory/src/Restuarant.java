public abstract class Restuarant {
    public void orderBurger()
    {
        System.out.println("Ordering Burger....");
        Burger burger = createBurger();
        burger.prepare();
    }

    public abstract Burger createBurger();
}
