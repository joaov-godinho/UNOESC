class CadastroController {
    constructor(view) {
        this.view = view;
        this.pessoas = [];

        this.view.setSubmitCallback((nome, idade, email) => {
            this.adicionarPessoa(nome, idade, email);
        });
    }

    adicionarPessoa(nome, idade, email) {
        const pessoa = new Pessoa(nome, idade, email);
        this.pessoas.push(pessoa);
        this.view.adicionarPessoaNaLista(pessoa);
    }
}