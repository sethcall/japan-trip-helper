document.addEventListener('DOMContentLoaded', () => {
    updateCountdown();
    fetchWeather();
    updateDynamicBanner();
});

function updateDynamicBanner() {
    const bannerElement = document.getElementById('dynamic-banner');
    const now = new Date();
    
    // Get Tokyo Time
    // We need to calculate the hour in Tokyo. 
    // Tokyo is UTC+9.
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const tokyoOffset = 9 * 60 * 60 * 1000;
    const tokyoDate = new Date(utc + tokyoOffset);
    const tokyoHour = tokyoDate.getHours();

    // Location Logic based on date (assuming 2025/2026 for the trip context)
    // Kyoto: Dec 26 - Dec 29
    // Note: JS Month is 0-indexed (11 = Dec)
    const year = tokyoDate.getFullYear();
    const month = tokyoDate.getMonth();
    const date = tokyoDate.getDate();

    let isKyoto = false;
    if (year === 2025 && month === 11) { // December 2025
        if (date >= 26 && date <= 29) {
            isKyoto = true;
        }
    }

    // Time of Day Logic (Tokyo Time)
    // Day: 5:00 AM - 5:00 PM
    // Evening: 5:00 PM - 9:00 PM
    // Night: 9:00 PM - 5:00 AM
    const isEvening = (tokyoHour >= 17 && tokyoHour < 21);
    const isNight = (tokyoHour >= 21 || tokyoHour < 5);
    // Otherwise it's day

    let imageSrc = '';

    if (isNight) {
        imageSrc = 'assets/webp/night.webp';
    } else if (isEvening) {
        if (isKyoto) {
            imageSrc = 'assets/gif/kyoto-evening.gif';
        } else {
            // Tokyo Evening: Random between two gifs
            const tokyoEveningImages = [
                'assets/gif/tokyo-evening.gif',
                'assets/gif/tokyo-evening-1.gif'
            ];
            const randomIndex = Math.floor(Math.random() * tokyoEveningImages.length);
            imageSrc = tokyoEveningImages[randomIndex];
        }
    } else {
        // Day
        if (isKyoto) {
            // Kyoto Day: Random between two webps
            const kyotoDayImages = [
                'assets/webp/kyoto-day.webp',
                'assets/webp/kyoto-day-1.webp'
            ];
            const randomIndex = Math.floor(Math.random() * kyotoDayImages.length);
            imageSrc = kyotoDayImages[randomIndex];
        } else {
            imageSrc = 'assets/webp/tokyo-day.webp';
        }
    }

    bannerElement.src = imageSrc;
}

function updateCountdown() {
    const statusElement = document.getElementById('trip-status');
    const now = new Date();
    
    // Target: Jan 1, 2026. Note: Month is 0-indexed (0=Jan).
    const departureDate = new Date(2026, 0, 1); 
    
    // Reset hours to midnight for accurate day calculation
    const currentMidnight = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const depMidnight = new Date(departureDate.getFullYear(), departureDate.getMonth(), departureDate.getDate());

    const diffTime = depMidnight - currentMidnight;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    let html = '';
    let className = 'status-normal';

    if (currentMidnight.getFullYear() > 2026 || (currentMidnight.getFullYear() === 2026 && currentMidnight.getDate() > 1)) {
        html = '<div class="status-text">Sigh. Til Next Time</div>';
        className = "status-over";
    } else if (diffDays === 0) { // Jan 1st
        html = '<div class="status-text">Sayonara (Sianora)</div>';
        className = "status-depart";
    } else if (diffDays === 1) { // Dec 31st
        html = '<div class="status-text">Last Day</div>';
        className = "status-warning";
    } else if (diffDays > 1) {
        html = `
            <div class="countdown-box">
                <div class="countdown-number">${diffDays}</div>
                <div class="countdown-label">days left</div>
            </div>
        `;
        className = "status-active";
    } else {
        html = '<div class="status-text">Sigh. Til Next Time</div>';
        className = "status-over";
    }

    statusElement.innerHTML = html;
    statusElement.className = `trip-status ${className}`;
}

async function fetchWeather() {
    const locations = [
        { name: 'Tokyo', lat: 35.6895, long: 139.6917, id: 'weather-tokyo', url: 'https://www.jma.go.jp/bosai/forecast/#area_code=130000&area_type=offices' },
        { name: 'Kyoto', lat: 35.0116, long: 135.7681, id: 'weather-kyoto', url: 'https://www.jma.go.jp/bosai/forecast/#area_code=260000&area_type=offices' }
    ];

    for (const loc of locations) {
        try {
            // Added sunrise,sunset to daily params
            const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${loc.lat}&longitude=${loc.long}&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=Asia%2FTokyo&forecast_days=3&temperature_unit=fahrenheit`);
            const data = await response.json();
            renderWeather(loc, data);
        } catch (error) {
            console.error(`Error fetching weather for ${loc.name}:`, error);
            document.getElementById(loc.id).innerHTML = '<p>Weather unavailable</p>';
        }
    }
}

function renderWeather(location, data) {
    const container = document.getElementById(location.id);
    
    // Parse Sunrise/Sunset for Today (index 0)
    const sunrise = data.daily.sunrise[0];
    const sunset = data.daily.sunset[0];
    
    const formatTime = (isoString) => {
        const date = new Date(isoString);
        return date.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
    };

    const sunriseTime = formatTime(sunrise);
    const sunsetTime = formatTime(sunset);

    let html = `<h3><a href="${location.url}" target="_blank">${location.name}</a></h3>`;
    
    // Insert Sun Times
    html += `
        <div class="sun-times" style="display: flex; justify-content: center; gap: 20px; margin-bottom: 15px; font-size: 0.95em; color: #555; background-color: #f8f9fa; padding: 5px; border-radius: 6px;">
            <span title="Sunrise">🌅 ${sunriseTime}</span>
            <span title="Sunset">🌇 ${sunsetTime}</span>
        </div>
    `;

    html += `<div class="forecast-grid">`;

    const daily = data.daily;
    const days = ['Today', 'Tomorrow', 'Day After'];

    daily.time.forEach((time, index) => {
        const code = daily.weathercode[index];
        const maxF = Math.round(daily.temperature_2m_max[index]);
        const minF = Math.round(daily.temperature_2m_min[index]);
        // Simple conversion back if we wanted C, but the prompt says just F or as well.
        // Let's just show F as requested.
        const icon = getWeatherIcon(code);
        const desc = getWeatherDesc(code);

        html += `
            <div class="forecast-day">
                <div class="day-name">${days[index]}</div>
                <div class="weather-icon" title="${desc}">${icon}</div>
                <div class="temps">
                    <span class="high">${maxF}°F</span> / <span class="low">${minF}°F</span>
                </div>
            </div>
        `;
    });

    html += '</div>';
    container.innerHTML = html;
}

function getWeatherIcon(code) {
    // WMO Weather interpretation codes (WW)
    // 0: Clear sky
    // 1, 2, 3: Mainly clear, partly cloudy, and overcast
    // 45, 48: Fog
    // 51, 53, 55: Drizzle
    // 61, 63, 65: Rain
    // 71, 73, 75: Snow
    // 80, 81, 82: Rain showers
    // 95, 96, 99: Thunderstorm

    if (code === 0) return '☀️';
    if (code <= 3) return '⛅';
    if (code <= 48) return '🌫️';
    if (code <= 67) return '🌧️';
    if (code <= 77) return '❄️';
    if (code <= 82) return '🌦️';
    if (code <= 99) return '⛈️';
    return '❓';
}

function getWeatherDesc(code) {
    if (code === 0) return 'Clear sky';
    if (code <= 3) return 'Cloudy';
    if (code <= 48) return 'Fog';
    if (code <= 67) return 'Rain';
    if (code <= 77) return 'Snow';
    return 'Precipitation';
}