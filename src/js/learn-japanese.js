document.addEventListener('DOMContentLoaded', () => {
    if (window.japaneseData) {
        initJapaneseWidgets();
        initFullLists();
    }
});

function initJapaneseWidgets() {
    new JapaneseWidget('word-widget', window.japaneseData.japaneseWords, 'Word of the Day');
    new JapaneseWidget('phrase-widget', window.japaneseData.japanesePhrases, 'Phrase of the Day');
}

function initFullLists() {
    const wordsContainer = document.getElementById('full-words-list');
    if (wordsContainer) {
        window.japaneseData.japaneseWords.forEach(item => {
            wordsContainer.innerHTML += renderListItem(item);
        });
    }

    const phrasesContainer = document.getElementById('full-phrases-list');
    if (phrasesContainer) {
        window.japaneseData.japanesePhrases.forEach(item => {
            phrasesContainer.innerHTML += renderListItem(item);
        });
    }
}

function renderListItem(item) {
    return `
        <div class="jp-widget-card" style="height: auto; min-height: 150px;">
            <div class="jp-content-area" style="margin-bottom: 0;">
                <div class="jp-text jp-japanese">${item.jp}</div>
                <div class="jp-text jp-phonetic">${item.phonetic}</div>
                <div class="jp-text jp-english">${item.en}</div>
            </div>
        </div>
    `;
}

class JapaneseWidget {
    constructor(elementId, data, title) {
        this.container = document.getElementById(elementId);
        if (!this.container) return;
        
        this.data = data;
        this.currentIndex = Math.floor(Math.random() * data.length);
        this.title = title;

        this.render();
        this.attachEvents();
    }

    render() {
        this.container.innerHTML = `
            <div class="jp-widget-card">
                <div class="jp-widget-title">${this.title}</div>
                <div class="jp-content-area">
                    <div class="jp-text jp-japanese fade-in">${this.data[this.currentIndex].jp}</div>
                    <div class="jp-text jp-phonetic fade-in">${this.data[this.currentIndex].phonetic}</div>
                    <div class="jp-text jp-english fade-in">${this.data[this.currentIndex].en}</div>
                </div>
                <div class="jp-controls">
                    <button class="jp-btn jp-prev">Prev</button>
                    <button class="jp-btn jp-next">Next</button>
                </div>
            </div>
        `;
    }

    attachEvents() {
        this.container.querySelector('.jp-prev').addEventListener('click', () => this.cycle(-1));
        this.container.querySelector('.jp-next').addEventListener('click', () => this.cycle(1));
    }

    cycle(direction) {
        const contentArea = this.container.querySelector('.jp-content-area');
        
        // Fade out
        contentArea.classList.add('fade-out');
        
        setTimeout(() => {
            this.currentIndex += direction;
            if (this.currentIndex < 0) this.currentIndex = this.data.length - 1;
            if (this.currentIndex >= this.data.length) this.currentIndex = 0;

            const item = this.data[this.currentIndex];
            
            // Update content
            this.container.querySelector('.jp-japanese').textContent = item.jp;
            this.container.querySelector('.jp-phonetic').textContent = item.phonetic;
            this.container.querySelector('.jp-english').textContent = item.en;

            // Remove fade out and trigger reflow for fade in
            contentArea.classList.remove('fade-out');
            
            // Optional: Trigger a new fade-in animation if needed, 
            // but removing fade-out usually snaps it back.
            // Let's use a keyframe animation class toggling if we want true fade-in/out every time.
            // For simplicity, we'll just toggle opacity classes.
        }, 300); // Match CSS transition time
    }
}
