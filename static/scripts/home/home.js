// Side Menu
const buttonSideBar = document.querySelector('.button-side-bar');
const sideBar = document.querySelector('.side-bar');
const icon = buttonSideBar.querySelector('i');

buttonSideBar.addEventListener('click', () => {
    buttonSideBar.classList.toggle('active');
    sideBar.classList.toggle('active');
    icon.classList.toggle('active');
})

// Add Post Button
const sideBarButton = document.getElementById('fazer_publicacao');
const buttonAddPostagem = document.querySelector('.button-add');
const iconAdd = document.querySelector('.button-content');
const iconAddI = buttonAddPostagem.querySelector('i');
const body = document.querySelector('body');
const divPost = document.querySelector('.div-post')

buttonAddPostagem.addEventListener('click', () => {
    body.classList.toggle('active');
    iconAddI.classList.toggle('active');
    divPost.classList.toggle('active');
    if (iconAddI.classList.contains('active')) {
        iconAdd.style.zIndex = 30;
    } else {
        iconAdd.style.zIndex = 21;
    }
});

sideBarButton.addEventListener('click', () => {
    body.classList.toggle('active');
    iconAddI.classList.toggle('active');
    divPost.classList.toggle('active');
    if (iconAddI.classList.contains('active')) {
        iconAdd.style.zIndex = 30;
    } else {
        iconAdd.style.zIndex = 21;
    }
});

// Icon Report and Comment
const reportIcon = document.getElementsByName('report-icon');
const seeIcon = document.getElementsByName('eye-icon');
const deleteIcon = document.getElementsByName('delete-icon');

reportIcon.forEach(reportIcon => {
    reportIcon.addEventListener('mouseover', () => {
        const reportField = reportIcon.closest('.report-field');
        if (!reportField.querySelector('p')) {
            const reportIconText = document.createElement('p');
            reportIconText.innerText = 'Reportar';
            reportIconText.classList.add('visible');
            reportField.appendChild(reportIconText);
            setTimeout(() => {
                reportIconText.classList.add('visible');
            }, 10);
        }
    });

    reportIcon.addEventListener('mouseout', () => {
        const reportField = reportIcon.closest('.report-field');
        const reportIconText = reportField.querySelector('p');
        if (reportIconText) {
            reportIconText.classList.remove('visible');
            setTimeout(() => {
                reportIconText.remove();
            }, 300);
        }
    });
});

seeIcon.forEach(seeIcon => {
    seeIcon.addEventListener('mouseover', () => {
        const seeField = seeIcon.closest('.see-field');
        if (!seeField.querySelector('p')) {
            const seeIconText = document.createElement('p');
            seeIconText.innerText = 'Visualizar';
            seeIconText.classList.add('visible');
            seeField.appendChild(seeIconText);
            setTimeout(() => {
                seeIconText.classList.add('visible');
            }, 10);
        }
    });

    seeIcon.addEventListener('mouseout', () => {
        const seeField = seeIcon.closest('.see-field');
        const seeIconText = seeField.querySelector('p');
        if (seeIconText) {
            seeIconText.classList.remove('visible');
            setTimeout(() => {
                seeIconText.remove();
            }, 300);
        }
    });
});


deleteIcon.forEach(deleteIcon => {
    deleteIcon.addEventListener('mouseover', () => {
        const deleteField = deleteIcon.closest('.delete-field');
        if (!deleteField.querySelector('p')) {
            const deleteIconText = document.createElement('p');
            deleteIconText.innerText = 'Excluir';
            deleteIconText.classList.add('visible');
            deleteField.appendChild(deleteIconText);
            setTimeout(() => {
                deleteIconText.classList.add('visible');
            }, 10);
        }
    });

    deleteIcon.addEventListener('mouseout', () => {
        const deleteField = deleteIcon.closest('.delete-field');
        const deleteIconText = deleteField.querySelector('p');
        if (deleteIconText) {
            deleteIconText.classList.remove('visible');
            setTimeout(() => {
                deleteIconText.remove();
            }, 300);
        }
    });
    deleteIcon.addEventListener('click', () => {
        const notdeleteButton = document.getElementById('not-delete-btn');
        const deleteDiv = document.querySelector('.div-delete')
        deleteDiv.classList.add('active');
        body.classList.add('active');

        notdeleteButton.addEventListener('click', () => {
            deleteDiv.classList.remove('active');
            body.classList.remove('active');
        });
    });
});

// Seleciona os elementos necessários
const deleteButtons = document.getElementsByName('delete-icon');
const deleteModal = document.getElementById('delete-modal');
const confirmDeleteButton = document.getElementById('confirm-delete-btn');
const notDeleteButton = document.getElementById('not-delete-btn');

let postIdToDelete = null;

// Adiciona o evento de clique a cada botão de exclusão
deleteButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        postIdToDelete = button.getAttribute('data-post-id');
        deleteModal.classList.add('active');
    });
});

// Confirmar a exclusão
confirmDeleteButton.addEventListener('click', () => {
    if (postIdToDelete) {
        window.location.href = `/home/excluir_postagem/${postIdToDelete}/`;
    }
});

// Fechar o modal sem excluir
notDeleteButton.addEventListener('click', (e) => {
    e.preventDefault();
    deleteModal.classList.remove('active');
});