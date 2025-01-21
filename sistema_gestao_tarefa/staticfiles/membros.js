document.addEventListener('DOMContentLoaded', function() {
    const membrosContainer = document.getElementById('membros-container');
    const membros = document.querySelectorAll('.membro-toggle');
    const selectedMembrosInput = document.getElementById('selected-membros');

    // Adiciona evento de clique às tags de membros
    membros.forEach(membro => {
        membro.addEventListener('click', function() {
            this.classList.toggle('bg-primary');
            this.classList.toggle('bg-secondary');
            updateSelectedMembros();
        });
    });

    function updateSelectedMembros() {
        const selectedMembros = Array.from(document.querySelectorAll('.membro-toggle.bg-primary'))
            .map(membro => membro.dataset.membroId);
        selectedMembrosInput.value = selectedMembros.join(',');
    }
});