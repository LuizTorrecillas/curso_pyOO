from livro import Livro


livro1 = Livro("O Alienista", "Machado de Assis", 1882)
livro2 = Livro("Quincas Borba", "Machado de Assis", 1891)
livro3 = Livro("O Cortiço", "Aluísio Azevedo", 1890)
livro4 = Livro("A Hora da Estrela", "Clarice Lispector", 1977)
livro5 = Livro("A Via Crucis do Corpo", "Clarice Lispector", 1977)

print("--- Exercício 6: Empréstimo ---")
print(f"Disponibilidade inicial de '{livro4.titulo}': {livro4.disponivel}")
livro4.emprestar()
print(f"Disponibilidade após emprestar: {livro4.disponivel}\n")

print("--- Exercício 7: Livros disponíveis em 1977 ---")
livros_1977 = Livro.verificar_disponibilidade(1977)

for livro in livros_1977:
    print(livro)