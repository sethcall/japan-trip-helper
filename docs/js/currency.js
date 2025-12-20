document.addEventListener('DOMContentLoaded', () => {
    setupCurrencyConverter();
});

function setupCurrencyConverter() {
    const yenInput = document.getElementById('yen-input');
    const usdInput = document.getElementById('usd-input');
    const RATE = 157; // 1 USD = 157 JPY

    if (!yenInput || !usdInput) return;

    yenInput.addEventListener('input', () => {
        const yen = parseFloat(yenInput.value);
        if (!isNaN(yen)) {
            const usd = yen / RATE;
            usdInput.value = usd.toFixed(2);
        } else {
            usdInput.value = '';
        }
    });

    usdInput.addEventListener('input', () => {
        const usd = parseFloat(usdInput.value);
        if (!isNaN(usd)) {
            const yen = usd * RATE;
            yenInput.value = Math.round(yen); // Yen usually no decimals
        } else {
            yenInput.value = '';
        }
    });
}
