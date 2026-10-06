/**
 * MR.FANTASTIC — Secure Portal Gateway Interactions
 */
document.addEventListener('DOMContentLoaded', () => {
    const authForm    = document.getElementById('login-form');
    const submitBtn   = document.getElementById('submitBtn');
    const statusDot   = document.getElementById('statusDot');
    const errorBanner = document.getElementById('errorBanner');

    // 1. TRIGGER SECURITY ALERT FLASH IF PASSWORDS CONFLICT
    if (errorBanner && statusDot) {
        statusDot.classList.add('breached');
        
        // Subtle cyber log indicator in developer tools console
        console.warn('System Gateway: Access Request Rejected. Keys mismatched.');
    }

    // 2. STABILIZE BUTTON TRANSITIONS UPON GATEWAY TRANSMISSION
    if (authForm && submitBtn) {
        authForm.addEventListener('submit', () => {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Verifying Keys...';
            submitBtn.style.background = '#801217';
            submitBtn.style.cursor = 'wait';
        });
    }
});