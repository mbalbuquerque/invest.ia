const toggle = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-menu');

if (toggle && mobileMenu) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    mobileMenu.hidden = open;
    toggle.textContent = open ? '☰' : '✕';
  });

  mobileMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      mobileMenu.hidden = true;
      toggle.textContent = '☰';
    });
  });
}

// PWA: registro do Service Worker e fluxo de instalação
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .catch((error) => console.error('Falha ao registrar o Service Worker:', error));
  });
}

let deferredInstallPrompt = null;
const installButtons = [
  document.getElementById('installApp'),
  document.getElementById('installAppMobile')
].filter(Boolean);

window.addEventListener('beforeinstallprompt', (event) => {
  event.preventDefault();
  deferredInstallPrompt = event;
  installButtons.forEach((button) => { button.hidden = false; });
});

installButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    if (!deferredInstallPrompt) return;
    deferredInstallPrompt.prompt();
    await deferredInstallPrompt.userChoice;
    deferredInstallPrompt = null;
    installButtons.forEach((item) => { item.hidden = true; });
  });
});

window.addEventListener('appinstalled', () => {
  deferredInstallPrompt = null;
  installButtons.forEach((button) => { button.hidden = true; });
});

// Carrossel de notícias do mercado
(() => {
  const track = document.getElementById('newsTrack');
  const prev = document.getElementById('newsPrev');
  const next = document.getElementById('newsNext');
  const dotsWrap = document.getElementById('newsDots');
  if (!track || !prev || !next || !dotsWrap) return;

  const cards = [...track.children];
  let index = 0;
  let autoTimer;

  const visibleCount = () => window.innerWidth <= 680 ? 1 : window.innerWidth <= 980 ? 2 : 3;
  const maxIndex = () => Math.max(0, cards.length - visibleCount());

  function cardStep() {
    const first = cards[0];
    if (!first) return 0;
    return first.getBoundingClientRect().width + 18;
  }

  function buildDots() {
    dotsWrap.innerHTML = '';
    for (let i = 0; i <= maxIndex(); i++) {
      const dot = document.createElement('button');
      dot.className = 'news-dot';
      dot.setAttribute('aria-label', `Ir para notícia ${i + 1}`);
      dot.addEventListener('click', () => { index = i; update(); restartAuto(); });
      dotsWrap.appendChild(dot);
    }
  }

  function update() {
    index = Math.min(index, maxIndex());
    track.style.transform = `translateX(-${index * cardStep()}px)`;
    [...dotsWrap.children].forEach((dot, i) => dot.classList.toggle('active', i === index));
  }

  function goNext() { index = index >= maxIndex() ? 0 : index + 1; update(); }
  function goPrev() { index = index <= 0 ? maxIndex() : index - 1; update(); }
  function restartAuto() { clearInterval(autoTimer); autoTimer = setInterval(goNext, 5200); }

  next.addEventListener('click', () => { goNext(); restartAuto(); });
  prev.addEventListener('click', () => { goPrev(); restartAuto(); });
  track.addEventListener('mouseenter', () => clearInterval(autoTimer));
  track.addEventListener('mouseleave', restartAuto);

  let touchStart = 0;
  track.addEventListener('touchstart', e => { touchStart = e.touches[0].clientX; }, {passive:true});
  track.addEventListener('touchend', e => {
    const delta = e.changedTouches[0].clientX - touchStart;
    if (Math.abs(delta) > 45) delta < 0 ? goNext() : goPrev();
    restartAuto();
  }, {passive:true});

  window.addEventListener('resize', () => { buildDots(); update(); });
  buildDots(); update(); restartAuto();
})();
