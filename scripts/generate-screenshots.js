const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const cardsDir = path.join(__dirname, '../src/cards');
const outputDir = path.join(__dirname, '../src/assets/cards');

(async () => {
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const files = fs.readdirSync(cardsDir).filter(file => file.endsWith('.html'));

    console.log(`Found ${files.length} cards to process.`);

    for (const file of files) {
        const filePath = path.join(cardsDir, file);
        const fileName = path.parse(file).name;
        const outputPath = path.join(outputDir, `${fileName}.png`);

        console.log(`Processing ${file}...`);

        const page = await browser.newPage();
        
        // Load the file. We use a file:// URL.
        const fileUrl = `file://${filePath}`;
        await page.goto(fileUrl, { waitUntil: 'networkidle0' });

        // Select the card element
        const element = await page.$('.address-card');

        if (element) {
            await element.screenshot({ path: outputPath });
            console.log(`Screenshot saved to ${outputPath}`);
        } else {
            console.error(`Could not find .address-card in ${file}`);
        }

        await page.close();
    }

    await browser.close();
    console.log('Done.');
})();
