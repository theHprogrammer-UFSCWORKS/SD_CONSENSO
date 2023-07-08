# Simulador Conceitual Difusão Atômica com Consenso Distribuído

O simulador de Difusão Atômica com Consenso Distribuído é uma aplicação GUI que simula o conceito do mesmo. O simulador foi desenvolvido como trabalho prático da disciplina de Sistemas Distribuídos do curso de Engenharia de Computação da Universidade Federal de Santa Catarina (UFSC), campus Araranguá.

O simulador foi desenvolvido utilizando a linguagem Python e a biblioteca tkinter para a interface gráfica.

-   [Como executar](#como-executar)
-   [Como utilizar](#como-utilizar)

## Como executar

Para executar o simulador, é necessário ter o Python 3 instalado. Em seguida, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

Para executar o simulador, execute o arquivo main.py:

```bash
python main.py
```

## Como utilizar

Ao executar o simulador, uma janela será aberta com a interface gráfica do simulador. A interface possui os seguintes elementos:

-   Clientes: Permite selecionar o número de clientes da simulação. Habilida o Num. Mensagens para cada cliente
-	Servidores: Permitee selecionar o número de servidores da simulação.
-   Num. Mensagens: Permite selecionar a quantidade de mensanges/requisições que cada cliente enviará ao servidor. Máx: 3

Após criar a simulação, a interface gráfica será reorganizada para exibir duas tabelas, clientes ao lado esquerdo e servidores ao lado direito.

-   Botão "Enviar Mensagens": Envia todas as mensangens de cada cliente de forma aleatória para todos os servidores.
-   Botão "Consenso Distribuído": Gera a votação entre os servidores para a ordem de resposta das mensagens.
-   Botão "Enviar Respostas": Todos os servidores respondem cada mensagem para seus respectivos cliente seguindo a ordem de consenso.

## Cloning this Repository

1. On GitHub.com, navigate to the repository's main page.
2. Above the list of files, click code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click 📋. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click 📋. To clone a repository using GitHub CLI, click Use GitHub CLI, then click 📋.
4. Open Git Bash.
5. Type git clone (clone git) and paste the URL you copied earlier.

```c
$ git clone
```

6. Press Enter to create your local clone.

<br>

## 👨‍💻 Author

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>
