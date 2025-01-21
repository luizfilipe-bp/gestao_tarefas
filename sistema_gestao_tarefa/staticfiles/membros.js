document.addEventListener('DOMContentLoaded', function () {
    const membrosContainer = document.getElementById('membros-container');
    const selectedMembrosInput = document.getElementById('selected-membros');

    if (!membrosContainer || !selectedMembrosInput) return;

    // Adiciona evento de clique para os membros
    membrosContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('membro-toggle')) {
            const membroBadge = event.target;
            membroBadge.classList.toggle('bg-primary');
            membroBadge.classList.toggle('bg-secondary');
            updateSelectedMembros();
        }
    });

    // Atualiza o campo hidden com os membros selecionados
    function updateSelectedMembros() {
        const selectedMembros = Array.from(document.querySelectorAll('.membro-toggle.bg-primary'))
            .map(membro => membro.dataset.membroId);
        selectedMembrosInput.value = selectedMembros.join(',');
    }
});
