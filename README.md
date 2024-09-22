
# Desafio Cadastro | Teste de Software I | 2024-02

Desafio proposto na disciplina de Teste de Software I - 2024-02.

# Descrição

A professora forneceu um código que estava com o teste quebrado na validação do campo de entrada de CPF, mas o que exatamente está quebrado?

Depois de testar se o algoritmo de validação de CPF estava correto, constatei que o erro era na clausúla de Assert apontando ```assert validar_cpf("123.456.789-09") == False ``` estava errada pois apesar desse CPF não pertencer a nenhum brasileiro, ele é matematicamente apto a passar o algoritmo.

Após coloca-lo como  ```assert validar_cpf("123.456.789-09") == True ``` o teste estava correto, adicionei alguns outros testes com números de CPF que realmente dariam ``False`` para garantir, mas no escopo do que era o problema o desafio foi resolvido.

Acabei criando um venv no Python pra rodar o Pytest mas não era necessário.

Print da execução do test_validacao com sucesso:

!["diagrama de classes com os pacotes"](https://i.imgur.com/nj7kA9X.png)

