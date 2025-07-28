// Confetti effect for perfect score
function fireConfetti() {
    if (typeof confetti !== 'undefined') {
        confetti({
            particleCount: 150,
            spread: 70,
            origin: { y: 0.6 }
        });
    }
}

// Animate score reveal
function animateScore(finalScore, maxScore, scoreElementId) {
    let el = document.getElementById(scoreElementId);
    if (!el) return;
    let current = 0;
    let step = Math.max(1, Math.floor(finalScore / 40));
    let interval = setInterval(() => {
        current += step;
        if (current >= finalScore) {
            current = finalScore;
            clearInterval(interval);
        }
        el.textContent = current + ' / ' + maxScore;
    }, 25);
}

// Ripple effect for buttons
function addRippleEffect() {
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function (e) {
            let circle = document.createElement('span');
            circle.className = 'ripple';
            let rect = btn.getBoundingClientRect();
            circle.style.left = (e.clientX - rect.left) + 'px';
            circle.style.top = (e.clientY - rect.top) + 'px';
            btn.appendChild(circle);
            setTimeout(() => circle.remove(), 600);
        });
    });
}

document.addEventListener('DOMContentLoaded', function () {
    addRippleEffect();
    // Animate question cards
    document.querySelectorAll('.question-card').forEach((card, i) => {
        card.style.opacity = 0;
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s';
            card.style.opacity = 1;
        }, 150 * i);
    });
});
