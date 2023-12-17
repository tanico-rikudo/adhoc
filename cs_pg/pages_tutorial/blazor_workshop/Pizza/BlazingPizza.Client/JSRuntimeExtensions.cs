using Microsoft.JSInterop;

namespace BlazingPizza.Client;


public static class JSRuntimeExtensions
{
    public static ValueTask<bool> Confirm(this IJSRuntime jsRuntime, string message)
    {
        // Implemented in example below
        return jsRuntime.InvokeAsync<bool>("confirm", message);
    }
}