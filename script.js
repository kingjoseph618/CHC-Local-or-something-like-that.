const header = document.querySelector('.site-header');
const menu = document.querySelector('.menu-toggle');
menu?.addEventListener('click', () => {
  const open = header.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
});
document.querySelectorAll('#primary-nav a').forEach(link => link.addEventListener('click', () => {
  header.classList.remove('open');
  menu?.setAttribute('aria-expanded', 'false');
}));

const progress = document.querySelector('.reading-line span');
function updateProgress() {
  const max = document.documentElement.scrollHeight - innerHeight;
  progress.style.width = `${max > 0 ? (scrollY / max) * 100 : 0}%`;
}
addEventListener('scroll', updateProgress, { passive: true });
updateProgress();

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
document.querySelector('#year').textContent = new Date().getFullYear();
