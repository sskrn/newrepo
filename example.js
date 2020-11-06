const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://test.widyaimersif.com');
  await page.screenshot({path: 'widya.png'});

  await browser.close();
})();
