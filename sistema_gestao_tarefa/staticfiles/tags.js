document.addEventListener('DOMContentLoaded', function() {
    const tagsContainer = document.getElementById('tags-container'); 
    const tags = document.querySelectorAll('.tag-toggle');
    const selectedTagsInput = document.getElementById('selected-tags');

    // Adiciona evento de clique às tags existentes
    tags.forEach(tag => {
        tag.addEventListener('click', function() {
            this.classList.toggle('bg-primary');
            this.classList.toggle('bg-secondary');
            updateSelectedTags();
        });
    });

    function updateSelectedTags() {
        const selectedTags = Array.from(document.querySelectorAll('.tag-toggle.bg-primary'))
            .map(tag => tag.textContent.trim());
        selectedTagsInput.value = selectedTags.join(',');
    }

    const novaTagInput = document.getElementById('nova_tag');
    novaTagInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const newTagName = this.value.trim();
            if (newTagName) {
                // Verifica se a tag já existe no contêiner
                const existingTag = Array.from(tagsContainer.children).find(
                    tag => tag.textContent.trim().toLowerCase() === newTagName.toLowerCase()
                );

                if (existingTag) {
                    // Marca a tag existente como selecionada
                    existingTag.classList.add('bg-primary');
                    existingTag.classList.remove('bg-secondary');
                } else {
                    // Cria uma nova tag e adiciona ao contêiner
                    const newTagSpan = document.createElement('span');
                    newTagSpan.className = 'badge bg-primary tag-toggle';
                    newTagSpan.textContent = newTagName;

                    // Adiciona o evento de clique na nova tag
                    newTagSpan.addEventListener('click', function() {
                        this.classList.toggle('bg-primary');
                        this.classList.toggle('bg-secondary');
                        updateSelectedTags();
                    });
                    tagsContainer.appendChild(newTagSpan);
                }
                this.value = ''; // Limpa o campo de entrada
                updateSelectedTags();
            }
        }
    });
});
