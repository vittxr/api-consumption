const btn_add = document.querySelector('.btn-add');
const resgister__box = document.querySelector('.user-register__box');
btn_add.addEventListener('click', openForm)

function openForm () {
    resgister__box.style.display = 'flex';
}

function close_() {
    resgister__box.style.display = 'none';
}