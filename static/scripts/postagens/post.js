// Side Menu

const buttonSideBar = document.querySelector('.button-side-bar');
const sideBar = document.querySelector('.side-bar');
const icon = buttonSideBar.querySelector('i');

buttonSideBar.addEventListener('click', () => {
    buttonSideBar.classList.toggle('active');
    sideBar.classList.toggle('active');
    icon.classList.toggle('active');
})

//Comment Page
const commentField = document.querySelector('.comment-field');
const commentIcon = document.getElementById('comment-icon');
const body = document.querySelector('body');

commentIcon.addEventListener('click', () => {
    body.classList.add('active', 'no-scroll');
    body.style.zIndex = 98;
    const commentPage = document.getElementById('comment-page');
    commentPage.classList.add('active');

    const buttonVoltar = document.getElementById('voltar');
    buttonVoltar.addEventListener('click', () => {
        body.classList.remove('active', 'no-scroll');
        body.style.zIndex = 1;
        commentPage.classList.remove('active');
    });
});