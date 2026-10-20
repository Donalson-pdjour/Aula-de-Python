
import tkinter as tk
from tkinter import messagebox


class Cadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Cadastro TabajaraCorp")
        self.master.geometry("650x600")
        self.master.resizable(False, False)

        # Lista que armazena os cadastros realizados
        self.cadastros = []

        # Variáveis de controle dos campos
        self.nome = tk.StringVar()
        self.sobrenome = tk.StringVar()
        self.idade = tk.StringVar()
        self.endereco = tk.StringVar()
        self.bairro = tk.StringVar()
        self.cidade = tk.StringVar()
        self.uf = tk.StringVar()
        self.sexo = tk.StringVar()
        self.telefone = tk.StringVar()
        self.email = tk.StringVar()
        self.rg = tk.StringVar()
        self.cpf = tk.StringVar()

        # Título da janela
        titulo = tk.Label(
            master,
            text="Cadastro de Pessoas",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        # Frame para organizar os campos
        frame = tk.Frame(master)
        frame.pack(padx=20, pady=5)

        # Configura as duas colunas
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

        # Função para criar rótulos e campos
        def criar_campo(rotulo, variavel, linha, coluna):
            tk.Label(
                frame,
                text=rotulo,
                font=("Arial", 10)
            ).grid(
                row=linha,
                column=coluna,
                sticky="w",
                padx=5,
                pady=7
            )

            entrada = tk.Entry(
                frame,
                textvariable=variavel,
                width=23
            )

            entrada.grid(
                row=linha,
                column=coluna + 1,
                padx=5,
                pady=7,
                sticky="ew"
            )

            return entrada

        # Campos do cadastro
        criar_campo("Nome:", self.nome, 0, 0)
        criar_campo("Sobrenome:", self.sobrenome, 0, 2)

        criar_campo("Idade:", self.idade, 1, 0)
        criar_campo("Endereço:", self.endereco, 1, 2)

        criar_campo("Bairro:", self.bairro, 2, 0)
        criar_campo("Cidade:", self.cidade, 2, 2)

        # Seleção do estado
        tk.Label(frame, text="UF:").grid(
            row=3, column=0, sticky="w", padx=5, pady=7
        )

        estados = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF",
            "ES", "GO", "MA", "MT", "MS", "MG", "PA",
            "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
            "RO", "RR", "SC", "SP", "SE", "TO"
        ]

        self.uf.set("RS")

        tk.OptionMenu(
            frame,
            self.uf,
            *estados
        ).grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5,
            pady=7
        )

        # Seleção do sexo
        tk.Label(frame, text="Sexo:").grid(
            row=3, column=2, sticky="w", padx=5, pady=7
        )

        frame_sexo = tk.Frame(frame)
        frame_sexo.grid(row=3, column=3, sticky="w")

        tk.Radiobutton(
            frame_sexo,
            text="Masculino",
            variable=self.sexo,
            value="Masculino"
        ).pack(side="left")

        tk.Radiobutton(
            frame_sexo,
            text="Feminino",
            variable=self.sexo,
            value="Feminino"
        ).pack(side="left")

        # Demais campos
        criar_campo("Telefone:", self.telefone, 4, 0)
        criar_campo("Email:", self.email, 4, 2)

        criar_campo("RG:", self.rg, 5, 0)
        criar_campo("CPF:", self.cpf, 5, 2)

        # Frame dos botões
        frame_botoes = tk.Frame(master)
        frame_botoes.pack(pady=20)

        tk.Button(
            frame_botoes,
            text="Salvar cadastro",
            width=18,
            command=self.salvar_cadastro
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botoes,
            text="Limpar campos",
            width=18,
            command=self.limpar_campos
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botoes,
            text="Ver cadastros",
            width=18,
            command=self.ver_cadastros
        ).pack(side="left", padx=5)

    # Método para salvar os dados
    def salvar_cadastro(self):
        # Obtém os valores dos campos
        nome = self.nome.get().strip()
        sobrenome = self.sobrenome.get().strip()
        idade = self.idade.get().strip()
        endereco = self.endereco.get().strip()
        bairro = self.bairro.get().strip()
        cidade = self.cidade.get().strip()
        uf = self.uf.get()
        sexo = self.sexo.get()
        telefone = self.telefone.get().strip()
        email = self.email.get().strip()
        rg = self.rg.get().strip()
        cpf = self.cpf.get().strip()

        # Verifica os campos obrigatórios
        if not nome or not sobrenome or not idade or not cpf:
            messagebox.showwarning(
                "Campos obrigatórios",
                "Preencha Nome, Sobrenome, Idade e CPF."
            )
            return

        # Valida a idade
        try:
            idade = int(idade)

            if idade < 1 or idade > 120:
                messagebox.showwarning(
                    "Idade inválida",
                    "Digite uma idade entre 1 e 120."
                )
                return

        except ValueError:
            messagebox.showwarning(
                "Idade inválida",
                "A idade deve conter apenas números inteiros."
            )
            return

        # Verifica se o CPF possui 11 dígitos
        cpf_numeros = "".join(
            caractere for caractere in cpf
            if caractere.isdigit()
        )

        if len(cpf_numeros) != 11:
            messagebox.showwarning(
                "CPF inválido",
                "O CPF deve conter 11 dígitos."
            )
            return

        # Organiza os dados em um dicionário
        cadastro = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "endereco": endereco,
            "bairro": bairro,
            "cidade": cidade,
            "uf": uf,
            "sexo": sexo,
            "telefone": telefone,
            "email": email,
            "rg": rg,
            "cpf": cpf
        }

        # Armazena o cadastro na lista
        self.cadastros.append(cadastro)

        # Exibe a confirmação
        messagebox.showinfo(
            "Cadastro realizado",
            f"Cadastro de {nome} {sobrenome} salvo com sucesso!"
        )

        # Limpa os campos depois de salvar
        self.limpar_campos()

    # Método para limpar os campos
    def limpar_campos(self):
        self.nome.set("")
        self.sobrenome.set("")
        self.idade.set("")
        self.endereco.set("")
        self.bairro.set("")
        self.cidade.set("")
        self.uf.set("RS")
        self.sexo.set("")
        self.telefone.set("")
        self.email.set("")
        self.rg.set("")
        self.cpf.set("")

    # Método para visualizar os cadastros
    def ver_cadastros(self):
        if not self.cadastros:
            messagebox.showinfo(
                "Cadastros",
                "Nenhum cadastro foi realizado."
            )
            return

        # Cria uma janela para exibir os registros
        janela_cadastros = tk.Toplevel(self.master)
        janela_cadastros.title("Cadastros realizados")
        janela_cadastros.geometry("500x400")

        tk.Label(
            janela_cadastros,
            text="Pessoas cadastradas",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Área de texto para apresentar os registros
        texto = tk.Text(
            janela_cadastros,
            width=55,
            height=20,
            wrap="word"
        )
        texto.pack(padx=10, pady=10)

        # Adiciona cada cadastro na área de texto
        for numero, cadastro in enumerate(self.cadastros, start=1):
            texto.insert(
                "end",
                f"Cadastro {numero}\n"
                f"Nome: {cadastro['nome']} {cadastro['sobrenome']}\n"
                f"Idade: {cadastro['idade']}\n"
                f"Endereço: {cadastro['endereco']}\n"
                f"Bairro: {cadastro['bairro']}\n"
                f"Cidade: {cadastro['cidade']} - {cadastro['uf']}\n"
                f"Sexo: {cadastro['sexo']}\n"
                f"Telefone: {cadastro['telefone']}\n"
                f"Email: {cadastro['email']}\n"
                f"RG: {cadastro['rg']}\n"
                f"CPF: {cadastro['cpf']}\n"
                f"{'-' * 40}\n"
            )

        # Impede a edição dos dados exibidos
        texto.config(state="disabled")


# Inicializa o programa
if __name__ == "__main__":
    janela = tk.Tk()
    app = Cadastro(janela)
    janela.mainloop()
