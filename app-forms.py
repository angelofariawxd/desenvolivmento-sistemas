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
