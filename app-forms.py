import sqlite3
import tkinter as tk
from tkinter import messagebox


# --- FUNÇÕES DE BANCO DE DADOS ---
def inicializar_banco():
    """Cria o banco de dados e a tabela de clientes caso não existam."""
    conexao = sqlite3.connect("cadastro_clientes.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """
    )
    conexao.commit()
    conexao.close()


def salvar_cliente():
    """Valida os campos e salva as informações no banco de dados."""
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação: Garante que todos os campos estejam preenchidos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Alerta", "Todos os campos devem ser preenchidos!"
        )
        return

    try:
        conexao = sqlite3.connect("cadastro_clientes.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone),
        )
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()

    except Exception as e:
        messagebox.showerror(
            "Erro", f"Erro ao salvar no banco de dados: {str(e)}"
        )


def limpar_formulario():
    """Limpa todos os campos de entrada de texto da interface."""
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.focus_set()


# --- INTERFACE GRÁFICA (TKINTER) ---
# Inicializa o banco de dados
inicializar_banco()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x250")
janela.resizable(False, False)

# Componentes da Interface (Labels e Entries)
lbl_nome = tk.Label(janela, text="Nome:", font=("Arial", 10, "bold"))
lbl_nome.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=15, pady=10)

lbl_email = tk.Label(janela, text="E-mail:", font=("Arial", 10, "bold"))
lbl_email.grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_email = tk.Entry(janela, width=35)
entry_email.grid(row=1, column=1, padx=15, pady=10)

lbl_telefone = tk.Label(janela, text="Telefone:", font=("Arial", 10, "bold"))
lbl_telefone.grid(row=2, column=0, padx=15, pady=10, sticky="w")
entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=2, column=1, padx=15, pady=10)

# Frame para alinhar os botões lado a lado
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)

# Botão Salvar
btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    bg="#4CAF50",
    fg="white",
    width=12,
    command=salvar_cliente,
)
btn_salvar.pack(side=tk.LEFT, padx=10)

# Botão Limpar
btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    bg="#f44336",
    fg="white",
    width=12,
    command=limpar_formulario,
)
btn_limpar.pack(side=tk.LEFT, padx=10)

# Executa o aplicativo
janela.mainloop()


import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# --- FUNÇÕES DE BANCO DE DADOS ---
def inicializar_banco():
    """Cria o banco de dados e a tabela de clientes caso não existam."""
    with sqlite3.connect("cadastro_clientes.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """
        )


def salvar_cliente():
    """Valida os campos e salva as informações no banco de dados."""
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Alerta", "Todos os campos devem ser preenchidos!"
        )
        return

    try:
        with sqlite3.connect("cadastro_clientes.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone),
            )

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()

    except Exception as e:
        messagebox.showerror(
            "Erro", f"Erro ao salvar no banco de dados: {str(e)}"
        )


def limpar_formulario():
    """Limpa todos os campos de entrada de texto da interface."""
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.focus_set()


def visualizar_clientes():
    """Abre uma nova janela e exibe a lista de todos os clientes cadastrados."""
    janela_visu = tk.Toplevel(janela)
    janela_visu.title("Clientes Cadastrados")
    janela_visu.geometry("600x300")
    janela_visu.grab_set()  # Mantém o foco na janela secundária

    colunas = ("ID", "Nome", "E-mail", "Telefone")
    tabela = ttk.Treeview(janela_visu, columns=colunas, show="headings")

    # Cabeçalhos
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("E-mail", text="E-mail")
    tabela.heading("Telefone", text="Telefone")

    # Colunas
    tabela.column("ID", width=40, anchor="center")
    tabela.column("Nome", width=180, anchor="w")
    tabela.column("E-mail", width=200, anchor="w")
    tabela.column("Telefone", width=120, anchor="center")

    # Barra de rolagem
    scrollbar = ttk.Scrollbar(
        janela_visu, orient=tk.VERTICAL, command=tabela.yview
    )
    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

    # Busca no banco de dados
    try:
        with sqlite3.connect("cadastro_clientes.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email, telefone FROM clientes")
            registros = cursor.fetchall()

        for cliente in registros:
            tabela.insert("", tk.END, values=cliente)

    except Exception as e:
        messagebox.showerror(
            "Erro",
            f"Erro ao carregar dados do banco de dados: {str(e)}",
            parent=janela_visu,
        )


# --- INTERFACE GRÁFICA ---
inicializar_banco()

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("420x250")
janela.resizable(False, False)

lbl_nome = tk.Label(janela, text="Nome:", font=("Arial", 10, "bold"))
lbl_nome.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=15, pady=10)

lbl_email = tk.Label(janela, text="E-mail:", font=("Arial", 10, "bold"))
lbl_email.grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_email = tk.Entry(janela, width=35)
entry_email.grid(row=1, column=1, padx=15, pady=10)

lbl_telefone = tk.Label(janela, text="Telefone:", font=("Arial", 10, "bold"))
lbl_telefone.grid(row=2, column=0, padx=15, pady=10, sticky="w")
entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=2, column=1, padx=15, pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)

btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    bg="#4CAF50",
    fg="white",
    width=10,
    command=salvar_cliente,
)
btn_salvar.pack(side=tk.LEFT, padx=5)

btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    bg="#f44336",
    fg="white",
    width=10,
    command=limpar_formulario,
)
btn_limpar.pack(side=tk.LEFT, padx=5)

btn_visualizar = tk.Button(
    frame_botoes,
    text="Visualizar",
    bg="#2196F3",
    fg="white",
    width=10,
    command=visualizar_clientes,
)
btn_visualizar.pack(side=tk.LEFT, padx=5)

janela.mainloop()
