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
const reportField = document.querySelector('.report-field');
const reportIcon = document.getElementById('report-icon');
const seeField = document.querySelector('.see-field');
const seeIcon = document.getElementById('eye-icon');

reportIcon.addEventListener('mouseover', () => {
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
    const reportIconText = reportField.querySelector('p');
    if (reportIconText) {
        reportIconText.classList.remove('visible');
        setTimeout(() => {
            reportIconText.remove();
        }, 300);
    }
});

seeIcon.addEventListener('mouseover', () => {
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
    const seeIconText = seeField.querySelector('p');
    if (seeIconText) {
        seeIconText.classList.remove('visible');
        setTimeout(() => {
            seeIconText.remove();
        }, 300);
    }
});