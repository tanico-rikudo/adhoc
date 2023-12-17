
namespace BlazingPizza.Client;
public class OrderState
{
    public Pizza? ConfiguringPizza { get; private set; }
    public bool ShowingConfigureDialog { get; private set; }
    public Order order = new Order();
    public void ShowConfigurePizzaDialog(PizzaSpecial special)
    {
        ConfiguringPizza = new Pizza()
        {
            Special = special,
            SpecialId = special.Id,
            Size = Pizza.DefaultSize,
            Toppings = new List<PizzaTopping>()
        };
        ShowingConfigureDialog = true;

    }

    public void CancelConfigurePizzaDialog()
    {
        ConfiguringPizza = null;
        ShowingConfigureDialog = false;
    }

    public void ConfirmConfigurePizzaDialog()
    {
        order.Pizzas.Add(ConfiguringPizza);
        ConfiguringPizza = null;
        ShowingConfigureDialog = false;
    }

    public void ResetOrder()
    {
        order = new Order();
    }

    public void RemoveConfiguredPizza(Pizza pizza)
    {
        order.Pizzas.Remove(pizza);
    }

    public void ReplaceOrder(Order order)
    {
        this.order = order;
    }

}