import random
import tkinter as tk
from tkinter import ttk


class Mensagem:
    def __init__(self, id, id_cliente):
        """
        Inicializa uma instância de Mensagem.

        Args:
            id (int): O identificador da mensagem.
            id_cliente (int): O identificador do cliente que enviou a mensagem.
        """
        self.id = id
        self.id_cliente = id_cliente
        self.status = "Não enviada"

    def __str__(self):
        """
        Retorna uma string que representa a mensagem.

        Returns:
            str: A representação da mensagem.
        """
        return f'Cliente {self.id_cliente} - Mensagem {self.id}: {self.status}'


class Cliente:
    def __init__(self, id):
        """
        Inicializa uma instância de Cliente.

        Args:
            id (int): O identificador do cliente.
        """
        self.id = id
        self.servidores = []
        self.mensagens = []
        self.respostas_recebidas = {}

    def adicionar_servidor(self, servidor):
        """
        Adiciona um servidor à lista de servidores do cliente.

        Args:
            servidor (Servidor): O servidor a ser adicionado.
        """
        self.servidores.append(servidor)

    def adicionar_mensagem(self, mensagem):
        """
        Adiciona uma mensagem à lista de mensagens do cliente.

        Args:
            mensagem (Mensagem): A mensagem a ser adicionada.
        """
        self.mensagens.append(mensagem)

    def enviar_mensagem(self):
        """
        Envia as mensagens do cliente para todos os servidores.
        """
        for mensagem in self.mensagens:
            for servidor in self.servidores:
                servidor.armazenar_mensagem(mensagem)

    def receber_resposta(self, mensagem):
        """
        Registra uma resposta recebida pelo cliente.

        Args:
            mensagem (Mensagem): A mensagem de resposta recebida.
        """
        if mensagem.id not in self.respostas_recebidas:
            self.respostas_recebidas[mensagem.id] = mensagem


class Servidor:
    def __init__(self, id):
        """
        Inicializa uma instância de Servidor.

        Args:
            id (int): O identificador do servidor.
        """
        self.id = id
        self.clientes = []
        self.mensagens_armazenadas = []
        self.mensagens_recebidas = []
        self.respostas_enviadas = []

    def adicionar_cliente(self, cliente):
        """
        Adiciona um cliente à lista de clientes do servidor.

        Args:
            cliente (Cliente): O cliente a ser adicionado.
        """
        self.clientes.append(cliente)

    def armazenar_mensagem(self, mensagem):
        """
        Armazena uma mensagem recebida pelo servidor.

        Args:
            mensagem (Mensagem): A mensagem a ser armazenada.
        """
        if mensagem not in self.mensagens_armazenadas:
            self.mensagens_armazenadas.append(mensagem)

    def receber_mensagens(self):
        """
        Recebe as mensagens armazenadas e as registra como mensagens recebidas pelo servidor.
        """
        random.shuffle(self.mensagens_armazenadas)
        for mensagem in self.mensagens_armazenadas:
            self.mensagens_recebidas.append(mensagem)
        self.mensagens_armazenadas = []

    def enviar_resposta(self, mensagem, proxima_mensagem):
        """
        Envia uma resposta a um cliente específico.

        Args:
            mensagem (Mensagem): A mensagem de resposta a ser enviada.
            proxima_mensagem (Mensagem): A próxima mensagem na ordem do consenso.
        """
        for cliente in self.clientes:
            if mensagem == proxima_mensagem and mensagem in cliente.mensagens and mensagem not in self.respostas_enviadas:
                self.respostas_enviadas.append(mensagem)
                cliente.receber_resposta(mensagem)


class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Simulação - Sistemas Distribuídos')

        self.limite_clientes = 3
        self.limite_servidores = 3
        self.limite_mensagens = 3

        self.cliente_selecionado = tk.StringVar()
        self.servidor_selecionado = tk.StringVar()
        self.mensagem_selecionada = {}

        self.cliente_selecionado.set(1)
        self.servidor_selecionado.set(1)

        self.criar_widgets()

    def criar_widgets(self):
        """
        Cria os widgets da aplicação.
        """
        ttk.Label(self, text="Número de Clientes:").grid(
            column=0, row=0, padx=10, pady=10)
        self.dropdown_cliente = ttk.Combobox(
            self, textvariable=self.cliente_selecionado)
        self.dropdown_cliente['values'] = list(
            range(1, self.limite_clientes + 1))
        self.dropdown_cliente.grid(column=1, row=0, padx=10, pady=10)
        self.dropdown_cliente.bind(
            "<<ComboboxSelected>>", self.atualizar_mensagens)

        ttk.Label(self, text="Número de Servidores:").grid(
            column=0, row=1, padx=10, pady=10)
        self.dropdown_servidor = ttk.Combobox(
            self, textvariable=self.servidor_selecionado)
        self.dropdown_servidor['values'] = list(
            range(1, self.limite_servidores + 1))
        self.dropdown_servidor.grid(column=1, row=1, padx=10, pady=10)

        self.botao_iniciar_simulacao = ttk.Button(
            self, text="Iniciar Simulação", command=self.iniciar_simulacao)
        self.botao_iniciar_simulacao.grid(
            column=0, row=3, columnspan=2, pady=10)

        self.labels_mensagem = []
        self.dropdowns_mensagem = []

    def atualizar_mensagens(self, event):
        """
        Atualiza a lista de mensagens exibida na interface com base no número de clientes selecionado.
        """
        for label in self.labels_mensagem:
            label.destroy()
        for dropdown in self.dropdowns_mensagem:
            dropdown.destroy()

        self.labels_mensagem = []
        self.dropdowns_mensagem = []
        self.mensagem_selecionada = {}

        num_clientes = int(self.cliente_selecionado.get())
        for i in range(num_clientes):
            label = ttk.Label(self, text=f"Cliente {i+1} Mensagens:")
            label.grid(column=0, row=2+i, padx=10, pady=10)
            self.labels_mensagem.append(label)

            var = tk.StringVar()
            var.set(1)
            self.mensagem_selecionada[i] = var

            dropdown = ttk.Combobox(self, textvariable=var)
            dropdown['values'] = list(range(1, self.limite_mensagens + 1))
            dropdown.grid(column=1, row=2+i, padx=10, pady=10)
            self.dropdowns_mensagem.append(dropdown)

        self.botao_iniciar_simulacao.grid(
            column=0, row=3+num_clientes, columnspan=2, pady=10)

    def iniciar_simulacao(self):
        """
        Inicia a simulação com base nos parâmetros selecionados pelo usuário.
        """
        num_clientes = int(self.cliente_selecionado.get())
        num_servidores = int(self.servidor_selecionado.get())

        JanelaSimulacao(self, num_clientes, num_servidores,
                        self.mensagem_selecionada)


class JanelaSimulacao(tk.Toplevel):
    def __init__(self, parent, num_clientes, num_servidores, mensagem_selecionada):
        super().__init__(parent)

        self.title('Simulação - Sistemas Distribuídos')

        self.clientes = [Cliente(i) for i in range(num_clientes)]
        self.servidores = [Servidor(i) for i in range(num_servidores)]

        for cliente in self.clientes:
            for servidor in self.servidores:
                cliente.adicionar_servidor(servidor)
                servidor.adicionar_cliente(cliente)

            num_mensagens = int(mensagem_selecionada[cliente.id].get())
            for i in range(num_mensagens):
                mensagem = Mensagem(i, cliente.id)
                cliente.adicionar_mensagem(mensagem)

        self.criar_widgets()

    def criar_widgets(self):
        """
        Cria os widgets da janela de simulação.
        """
        self.grid_columnconfigure(0, weight=1)  # Faz a coluna 0 expansível
        self.grid_columnconfigure(1, weight=1)  # Faz a coluna 1 expansível

        self.tabelas_cliente = []

        for cliente in self.clientes:
            tabela_cliente = ttk.Treeview(self, columns=(
                'Cliente', 'ID da Mensagem', 'Status'), show='headings')
            tabela_cliente.heading('Cliente', text='Cliente')
            tabela_cliente.heading('ID da Mensagem', text='ID da Mensagem')
            tabela_cliente.heading('Status', text='Status')

            for mensagem in cliente.mensagens:
                tabela_cliente.insert('', 'end', values=(
                    f"Cliente {cliente.id+1}", mensagem.id+1, mensagem.status))

            tabela_cliente.grid(row=cliente.id+1, column=0, padx=10, pady=10)
            self.tabelas_cliente.append(tabela_cliente)

        self.tabelas_servidor = []
        for servidor in self.servidores:
            tabela_servidor = ttk.Treeview(self, columns=(
                'Servidor', 'Mensagens Recebidas', 'Sugestão de Consenso', 'Consenso de Mensagens', 'Respostas'), show='headings')
            tabela_servidor.heading('Servidor', text='Servidor')
            tabela_servidor.heading('Mensagens Recebidas',
                                    text='Mensagens Recebidas')
            tabela_servidor.heading('Sugestão de Consenso',
                                    text='Sugestão de Consenso')
            tabela_servidor.heading('Consenso de Mensagens',
                                    text='Consenso de Mensagens')
            tabela_servidor.heading('Respostas',
                                    text='Respostas')

            tabela_servidor.insert('', 'end', values=(
                f"Servidor {servidor.id+1}", "Aguardando", "Aguardando", "Aguardando", "Aguardando"))

            tabela_servidor.grid(row=servidor.id+1, column=1, padx=10, pady=10)
            self.tabelas_servidor.append(tabela_servidor)

        self.botao_enviar_mensagens = ttk.Button(
            self, text="Enviar Mensagens", command=self.enviar_mensagens)
        self.botao_enviar_mensagens.grid(
            column=0, row=len(self.clientes)+2, pady=10)

        self.botao_consenso = ttk.Button(
            self, text="Consenso", command=self.executar_consenso)
        self.botao_consenso.grid(
            column=1, row=len(self.clientes)+2, pady=10)

        # Criar a barra de progresso
        # Cria uma variável double para atualizar a barra de progresso
        self.var_progresso = tk.DoubleVar()
        self.barra_progresso = ttk.Progressbar(
            self, length=200, variable=self.var_progresso, maximum=100)
        self.barra_progresso.grid(column=0, row=len(
            self.clientes)+4, columnspan=2, pady=10)

        self.botao_enviar_respostas = ttk.Button(
            self, text="Enviar Respostas", command=self.iniciar_envio_respostas)
        self.botao_enviar_respostas.grid(
            column=1, row=len(self.clientes)+3, pady=10)

    def enviar_mensagens(self):
        """
        Envia as mensagens dos clientes para os servidores.
        """
        # Embaralhar aleatoriamente as mensagens de cada cliente
        for cliente in self.clientes:
            random.shuffle(cliente.mensagens)

        # Embaralhar aleatoriamente os clientes para enviar mensagens em ordem aleatória
        random.shuffle(self.clientes)

        for cliente in self.clientes:
            cliente.enviar_mensagem()

        for servidor in self.servidores:
            servidor.receber_mensagens()

        # Atualizar a GUI
        for i, cliente in enumerate(self.clientes):
            for j, item in enumerate(self.tabelas_cliente[i].get_children()):
                self.tabelas_cliente[i].set(item, 'Status', 'Enviada')

        for i, servidor in enumerate(self.servidores):
            for j, item in enumerate(self.tabelas_servidor[i].get_children()):
                ids_mensagens = [f"M{mensagem.id+1}-{mensagem.id_cliente+1}"
                                 for mensagem in servidor.mensagens_recebidas]
                self.tabelas_servidor[i].set(
                    item, 'Mensagens Recebidas', ', '.join(ids_mensagens))

    def executar_consenso(self):
        """
        Executa o algoritmo de consenso nos servidores.
        """
        sugestoes_consenso = []

        # Embaralhar a lista de mensagens de cada servidor e adicionar as sugestões na lista sugestoes_consenso
        for servidor in self.servidores:
            random.shuffle(servidor.mensagens_recebidas)
            sugestoes_consenso.append(servidor.mensagens_recebidas)

        # Selecionar aleatoriamente uma das listas de mensagens como a ordem do consenso
        self.ordem_consenso = random.choice(sugestoes_consenso).copy()

        # Atualizar a GUI
        for i, servidor in enumerate(self.servidores):
            for j, item in enumerate(self.tabelas_servidor[i].get_children()):
                ids_sugestoes_consenso = [
                    f"M{mensagem.id+1}-{mensagem.id_cliente+1}" for mensagem in sugestoes_consenso[i]]
                self.tabelas_servidor[i].set(
                    item, 'Sugestão de Consenso', ', '.join(ids_sugestoes_consenso))

                ids_consenso = [
                    f"M{mensagem.id+1}-{mensagem.id_cliente+1}" for mensagem in self.ordem_consenso]
                self.tabelas_servidor[i].set(
                    item, 'Consenso de Mensagens', ', '.join(ids_consenso))

    def iniciar_envio_respostas(self):
        """
        Inicia o envio das respostas dos servidores para os clientes.
        """
        self.respostas_enviadas = 0
        self.respostas_servidor = ['' for _ in range(len(self.servidores))]
        self.proxima_mensagem = iter(self.ordem_consenso.copy())

        self.enviar_proxima_resposta()

    def enviar_proxima_resposta(self):
        """
        Envia a próxima resposta de um servidor para os clientes.
        """
        try:
            proxima_mensagem = next(self.proxima_mensagem)
            for servidor in self.servidores:
                servidor.enviar_resposta(proxima_mensagem, proxima_mensagem)
                # Atualizar as respostas do servidor na GUI
                if proxima_mensagem in servidor.respostas_enviadas:
                    self.respostas_servidor[servidor.id] += f"M{proxima_mensagem.id+1}-{proxima_mensagem.id_cliente+1}, "

            self.respostas_enviadas += 1
            self.atualizar_progresso()

            # Enviar a próxima resposta após um atraso
            self.after(1000, self.enviar_proxima_resposta)
        except StopIteration:
            print("Todas as respostas foram enviadas!")

    def atualizar_progresso(self):
        """
        Atualiza a barra de progresso e as tabelas da GUI com base no progresso do envio de respostas.
        """
        progresso = (self.respostas_enviadas / len(self.ordem_consenso)) * 100
        self.var_progresso.set(progresso)

        for i, cliente in enumerate(self.clientes):
            for j, mensagem in enumerate(self.ordem_consenso):
                # Se a mensagem foi enviada para o cliente, atualize o status
                if mensagem.id_cliente == cliente.id:
                    status = 'Respondida' if mensagem.id in cliente.respostas_recebidas else 'Enviada'
                    # Encontre o item correspondente na tabela do cliente e atualize o status
                    for item in self.tabelas_cliente[i].get_children():
                        if int(self.tabelas_cliente[i].set(item, 'ID da Mensagem')) == mensagem.id + 1:
                            self.tabelas_cliente[i].set(item, 'Status', status)
                            break

        for i, servidor in enumerate(self.servidores):
            for j, item in enumerate(self.tabelas_servidor[i].get_children()):
                self.tabelas_servidor[i].set(
                    item, 'Respostas', self.respostas_servidor[i])


if __name__ == "__main__":
    aplicacao = Aplicacao()
    aplicacao.mainloop()
