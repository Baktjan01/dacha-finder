const tg = window.Telegram.WebApp;
tg.ready();

const user = tg.initDataUnsafe?.user;

if (user) {
    // Настоящий Telegram (мобильный)
    fetch('/api/users/auth/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({user})
    })
        .then(res => res.json())
        .then(data => {
            window.currentUserId = data.user_id;
            window.currentTelegramId = data.telegram_id;
        });
} else {
    // Десктоп или браузер — гостевой режим
    window.currentUserId = null;
    window.currentTelegramId = null;
    console.log('Гостевой режим');
}

function showPage(name) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById('page-' + name).classList.add('active');
    document.getElementById('tab-' + name).classList.add('active');
}

// ── Filter ──
let filterOpen = false;

function toggleFilter() {
    filterOpen = !filterOpen;
    document.getElementById('filterPanel').classList.toggle('open', filterOpen);
}

function applyFilter() {
    toggleFilter();
}

// ── Modal ──
function openModal(id) {
    document.getElementById('modalOverlay').classList.add('open');
}

function closeModal(e) {
    if (e.target === document.getElementById('modalOverlay')) document.getElementById('modalOverlay').classList.remove('open');
}

// ── Submit ──
function submitDacha() {
    const title = document.getElementById('fTitle').value.trim();
    const location = document.getElementById('fLocation').value.trim();
    const price = document.getElementById('fPrice').value;
    const phone = document.getElementById('fPhone').value.trim();
    if (!title || !location || !price || !phone) {
        showToast('Заполните обязательные поля *');
        return;
    }
    // твоя логика отправки на сервер
}

// ── Helpers ──
function fmt(n) {
    return Number(n).toLocaleString('ru-RU');
}

function esc(s) {
    if (!s) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2800);
}