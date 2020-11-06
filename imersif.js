const puppeteer = require('puppeteer');

(async () => {
  //const browser = await puppeteer.launch();
  const browser = await puppeteer.launch({
    headless: true,
    //executablePath: '/usr/bin/chromium-browser',
    args: [ '--use-fake-ui-for-media-stream' ]
  });
//   const browser = await puppeteer.launch({
//     args: [ '--use-fake-ui-for-media-stream' ]
// })
  const page = await browser.newPage();
  await page.goto('https://test.widyaimersif.com');
  await page.screenshot({path: 'widya1.png'});
  
  await page.type('#roomName', '1234');
  await page.type('#userName', 'coba');

  await page.screenshot({path: 'widya2.png'});

  await page.click('#root > div > div > button');

  const context = browser.defaultBrowserContext();
  await context.overridePermissions('https://test.widyaimersif.com', ['camera','microphone'] );

  await page.waitForNavigation();

  await page.screenshot({path: 'widya3.png'});

  console.log('New Page URL:', page.url());
})();
