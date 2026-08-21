class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self) -> str:
        """Retorna uma representação em texto formatada do livro."""
        return (
            f"--- Detalhes do Livro ---\n"
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}"
        )


def cadastrar_livro():
    print("=== Cadastro de Livro na Biblioteca Digital ===")
    
    # Coleta de dados do usuário
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    
    # Validação simples para o número de páginas
    while True:
        try:
            paginas = int(input("Digite a quantidade de páginas: "))
            if paginas > 0:
                break
            print("Por favor, digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    # Instanciação do objeto e exibição através do __str__()
    novo_livro = Livro(titulo, autor, paginas)
    
    print("\nConfirmação dos dados:")
    # Chamada implícita do método __str__() via print()
    print(novo_livro)


if __name__ == "__main__":
    cadastrar_livro()
