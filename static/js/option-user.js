//Esse arquivo serve para abrir as opções de cada usuário (delete e update)
class OptionUser {
    constructor (index) {
        this.isCreated()
           //método para evitar de criar mais elementos, se um já estiver criado.

        this.div = document.createElement("div")
        this.div.classList.add("class", "options-user")

        //opcao alterar usuario:
        const span_change = document.createElement('span');
        span_change.innerText = 'Alterar dados';
        span_change.addEventListener('click', function() {
            //reutilizar o form de addUser para isso!!
            changeUser(index)
        })

         //opcao deletar usuário:
        const span_delete = document.createElement('span');
        span_delete.innerText = 'Deletar usuário';
        span_delete.addEventListener('click', function () { 
            deleteUser(index);
        })

        this.div.append(span_change)
        this.div.append(span_delete)

        let user = document.querySelectorAll('.user');
        user[index].append(this.div)

        document.querySelector('.backdrop').addEventListener('click', this.close)
    }

    close() { 
        document.querySelector(".options-user").remove();
        document.querySelector('.backdrop').style.display = 'none';
    }

    isCreated() {
        if (document.querySelector('.options-user') != null) {
            throw console.error("options-user já está criado!");
        }
    }
}

let user = document.querySelectorAll('.user');
let backdrop = document.querySelector('.backdrop');
user.forEach((e, index) => {
    user[index].addEventListener('click', function (e) {
        backdrop.style.display = 'block';
        console.log(backdrop)

        const option = new OptionUser(index);
           //precisa-se do index do elemento, para saber em qual div o elemento criado por OptionUser será inserido.
        console.log(option);
        e.preventDefault();
    }, false)
})