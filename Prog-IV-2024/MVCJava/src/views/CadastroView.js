class CadastroView {
    constructor() {
        this.form = document.querySelector("#cadastroForm");
        this.nomeInput = document.querySelector("#nome");
        this.idadeInput = document.querySelector("#idade");
        this.emailInput = document.querySelector("#email");
        this.listaPessoas = document.querySelector("#listaPessoas");

        this.form.addEventListener("submit", (event) => {
            event.preventDefault();
            this.onSubmit();
        });
    }

    onSubmit() {
        const nome = this.nomeInput.value;
        const idade = this.idadeInput.value;
        const email = this.emailInput.value;

        if (this.submitCallback) {
            this.submitCallback(nome, idade, email);
        }
    }

    setSubmitCallback(callback) {
        this.submitCallback = callback;
    }

    adicionarPessoaNaLista(pessoa) {
        const item = document.createElement("li");
        item.textContent = ${pessoa.nome} - ${pessoa.idade} anos - ${pessoa.email};
        this.listaPessoas.appendChild(item);
    }
}