document.addEventListener('DOMContentLoaded', () => {
    const helpIcon = document.getElementById('help-icon');
    
    helpIcon.addEventListener('click', () => {
        startTour(true);
    });

    // Small delay to ensure rendering
    setTimeout(() => {
        startTour(false);
    }, 500);
});

let currentStep = 0;
let isForced = false;

const tourSteps = [
    {
        targetSelector: '.location-name', // Points to the first location link
        text: "Click here to get a 'Address Card' that you could show a Japanese taxi driver.",
        storageKey: 'hide-location-tip',
        position: 'right' // Preferred position
    },
    {
        targetSelector: '.instruction-link', // Points to the first instruction link
        text: "Click here for all the instructions from Kelly, and additional tips, tricks, and things to do afterwards, for this destination.",
        storageKey: 'hide-tips-tip',
        position: 'right'
    }
];

function startTour(force) {
    isForced = force;
    currentStep = 0;
    showNextStep();
}

function showNextStep() {
    // Clean up previous popup
    removePopup();

    if (currentStep >= tourSteps.length) {
        return; // Tour done
    }

    const step = tourSteps[currentStep];
    
    // Check if we should skip this step (unless forced)
    if (!isForced && localStorage.getItem(step.storageKey) === 'true') {
        currentStep++;
        showNextStep();
        return;
    }

    const target = document.querySelector(step.targetSelector);
    if (!target) {
        console.warn('Tour target not found:', step.targetSelector);
        currentStep++;
        showNextStep();
        return;
    }

    createPopup(target, step);
}

function createPopup(target, step) {
    // Scroll target into view
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Highlight target
    target.classList.add('highlight-element');

    const popup = document.createElement('div');
    popup.className = 'tour-popup arrow-left'; // Defaulting to arrow-left style for side positioning
    
    // Determine visibility of "Don't show again"
    const showDontShow = !isForced; 

    const contentHtml = `
        <div class="popup-content">${step.text}</div>
        <div class="popup-actions">
            <button class="popup-btn" id="tour-next-btn">${currentStep === tourSteps.length - 1 ? 'Close' : 'Next'}</button>
            ${showDontShow ? `
            <label class="dont-show-label">
                <input type="checkbox" id="tour-dont-show-cb"> Don't show me this again
            </label>
            ` : ''}
        </div>
    `;

    popup.innerHTML = contentHtml;
    document.body.appendChild(popup);

    // Positioning logic (Basic implementation)
    const rect = target.getBoundingClientRect();
    const scrollY = window.scrollY;
    const scrollX = window.scrollX;

    // Position to the right of the element
    let top = rect.top + scrollY + (rect.height / 2) - (popup.offsetHeight / 2); // Center vertically? 
    // Actually, offsetHeight is 0 until rendered. 
    // Let's render first (display:block is set by class but we need to override the css 'none')
    popup.style.display = 'block';
    
    // Recalculate top with actual height
    top = rect.top + scrollY + (rect.height / 2) - (popup.offsetHeight / 2);
    let left = rect.right + scrollX + 15; // 15px gap

    // Check if it fits on screen, otherwise put it below
    if (left + popup.offsetWidth > window.innerWidth) {
        // Put it below
        popup.className = 'tour-popup arrow-top';
        left = rect.left + scrollX;
        top = rect.bottom + scrollY + 15;
    }

    popup.style.top = `${top}px`;
    popup.style.left = `${left}px`;

    // Event Listeners
    const nextBtn = document.getElementById('tour-next-btn');
    const dontShowCb = document.getElementById('tour-dont-show-cb');

    nextBtn.addEventListener('click', () => {
        if (dontShowCb && dontShowCb.checked) {
            localStorage.setItem(step.storageKey, 'true');
        }
        
        // Remove highlight
        target.classList.remove('highlight-element');
        
        currentStep++;
        showNextStep();
    });
}

function removePopup() {
    const existing = document.querySelector('.tour-popup');
    if (existing) {
        existing.remove();
    }
    // Remove all highlights just in case
    document.querySelectorAll('.highlight-element').forEach(el => {
        el.classList.remove('highlight-element');
    });
}
