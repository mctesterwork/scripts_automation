using Microsoft.Playwright;

/* Este es un script simple de pruebas con Playwright y C#, donde:
1. Se abre la página ebay.com
2. Busca y selecciona la opción llamada 'Mi eBay' (Esquina superior derecha)
3. Toma un screenshot del resultado y lo guarda
*/

using var playwright = await Playwright.CreateAsync();
await using var browser = await playwright.Chromium.LaunchAsync(new BrowserTypeLaunchOptions
{
    Headless = false,
    SlowMo = 50,
});
var page = await browser.NewPageAsync();
await page.GotoAsync("https://ebay.com");
var miEbay = page.Locator("#gh-eb-My .gh-eb-li-a");
await miEbay.HoverAsync();
await miEbay.ClickAsync();
await page.ScreenshotAsync(new PageScreenshotOptions { Path = "screenshot_mi_eBay.png" });