using BlazingPizza.Client;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Authentication;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using Microsoft.Extensions.DependencyInjection;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");

// page title
builder.RootComponents.Add<HeadOutlet>("head::after");

// add Base HttpClient to DI
builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });

// add OrdersClient to DI 
// BaseAddressAuthorizationMessageHandler will add the access token to the request, 
// not needed for default auth state (not need query token)
builder.Services.AddHttpClient<OrdersClient>(client => client.BaseAddress = new Uri(builder.HostEnvironment.BaseAddress))
        .AddHttpMessageHandler<BaseAddressAuthorizationMessageHandler>();
// add Order State to DI
builder.Services.AddScoped<OrderState>();

// add auth services
// builder.Services.AddApiAuthorization(); //default auth state
builder.Services.AddApiAuthorization<PizzaAuthenticationState>(options =>
{
    options.AuthenticationPaths.LogOutSucceededPath = "";
});

await builder.Build().RunAsync();
