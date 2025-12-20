document.addEventListener('DOMContentLoaded', () => {
    setupImageModal();
});

function setupImageModal() {
    const modal = document.getElementById('image-modal');
    const img = document.getElementById('phrases-thumbnail');
    const modalImg = document.getElementById('full-size-image');
    const link = document.getElementById('view-full-size');
    const closeBtn = document.querySelector('.close-modal');

    if (!modal || !img || !modalImg) return;

    function openModal() {
        modal.style.display = "block";
        modalImg.src = img.src;
    }

    img.onclick = openModal;
    
    if (link) {
        link.onclick = (e) => {
            e.preventDefault();
            openModal();
        }
    }

    if (closeBtn) {
        closeBtn.onclick = function() {
            modal.style.display = "none";
        }
    }
    
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
