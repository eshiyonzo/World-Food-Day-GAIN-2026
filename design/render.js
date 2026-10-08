const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + process.cwd() + '/' + f + '.html', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: f + '.pdf', width: '420mm', height: '297mm', printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
  }
  await b.close();
})();
