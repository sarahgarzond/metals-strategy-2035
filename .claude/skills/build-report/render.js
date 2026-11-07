// Usage: node render.js <input.html> <output.pdf>
const { chromium } = require('playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await page.pdf({
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    margin: { top: '18mm', bottom: '18mm', left: '20mm', right: '20mm' },
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-family:Inter,Arial;font-size:7.5px;color:#26307A;padding:0 20mm;display:flex;justify-content:space-between;">
      <span>Product Strategy 2035 &nbsp;|&nbsp; Growth Strategy for High Performance Metals</span>
      <span class="pageNumber"></span></div>`,
  });
  await browser.close();
})();
