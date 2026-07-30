class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __lt__(self, other):
        return self.titulo < other.titulo

    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}"

# Criando uma lista de livros
biblioteca = [
    Livro("1984", "George Orwell", 1949),
    Livro("Brave New World", "Aldous Huxley", 1932),
    Livro("The Catcher in the Rye", "J.D. Salinger", 1951)
]

# Ordenação por título (ordem natural)
biblioteca.sort()
print("Ordenação por título:")
for livro in biblioteca:
    print(livro)
    
# Ordenação por ano de publicação
biblioteca_sorted_ano = sorted(biblioteca, key=lambda livro: livro.ano_publicacao)
print("\nOrdenação por ano de publicação:")
for livro in biblioteca_sorted_ano:
    print(livro)

# Ordenação por autor
biblioteca_sorted_autor = sorted(biblioteca, key=lambda livro: livro.autor)
print("\nOrdenação por autor:")
for livro in biblioteca_sorted_autor:
    print(livro)
