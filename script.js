const languageToggle = document.querySelector('.language-toggle');

languageToggle.addEventListener('click', () => {
  const useEnglish = document.documentElement.lang !== 'en';
  document.documentElement.lang = useEnglish ? 'en' : 'zh-CN';
  document.querySelectorAll('[data-zh][data-en]').forEach((element) => {
    element.textContent = element.dataset[useEnglish ? 'en' : 'zh'];
  });
  languageToggle.textContent = useEnglish ? '中' : 'EN';
  languageToggle.setAttribute('aria-pressed', String(useEnglish));
  languageToggle.setAttribute('aria-label', useEnglish ? '切换到中文' : 'Switch to English');
  document.title = useEnglish ? 'XXX | Personal Website' : 'XXX | 个人主页';
});
