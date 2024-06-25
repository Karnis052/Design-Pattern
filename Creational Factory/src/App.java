public class App {
    public static void main(String[] args){
        Restuarant beefResto = new BeefBurgerRestuarant();
        beefResto.orderBurger();

        Restuarant veggieResto = new VeggieBurgerRestuarant();
        veggieResto.orderBurger();
    }
}
