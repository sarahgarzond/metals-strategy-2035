// Usage: node render.js <input.html> <output.pdf> [noheader]
// A4, 2.5 cm margins, page number top right in Times New Roman 12 (as in the team's Google Doc).
const { chromium } = require('playwright');
(async () => {
  const [inp, out, mode] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await page.pdf({
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: mode !== 'noheader',
    margin: { top: '25mm', bottom: '25mm', left: '25mm', right: '25mm' },
    headerTemplate: `<div style="width:100%;padding:0 25mm;margin-top:12.5mm;text-align:right;font-family:'Times New Roman','Liberation Serif',serif;font-size:12pt;color:#000;"><span class="pageNumber"></span></div>`,
    footerTemplate: '<span></span>',
  });
  await browser.close();
})();
