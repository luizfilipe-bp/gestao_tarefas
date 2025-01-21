document.addEventListener('DOMContentLoaded', () => {
    const toggleThemeButton = document.getElementById('toggleTheme');

    const temaSalvo = localStorage.getItem('tema') || 'dark';
    if (temaSalvo === 'light') {
        document.body.classList.add('light-mode');
        toggleThemeButton.textContent = 'Modo Escuro';
        toggleThemeButton.classList.replace('btn-outline-light', 'btn-outline-dark');
    }

    toggleThemeButton.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        if (document.body.classList.contains('light-mode')) {
            toggleThemeButton.textContent = 'Modo Escuro';
            toggleThemeButton.classList.replace('btn-outline-light', 'btn-outline-dark');
            localStorage.setItem('tema', 'light');
        } else {
            toggleThemeButton.textContent = 'Modo Claro';
            toggleThemeButton.classList.replace('btn-outline-dark', 'btn-outline-light');
            localStorage.setItem('tema', 'dark'); 
        }
    });
});
