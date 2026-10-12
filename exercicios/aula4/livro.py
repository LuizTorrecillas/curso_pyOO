class Livro:
    
    livros = []

    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        
        Livro.livros.append(self)

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao}) - Status: {status}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano: int) -> list:
        return [
            livro for livro in Livro.livros 
            if livro.ano_publicacao == ano and livro.disponivel
        ]

if __name__ == "__main__":
    print("--- Exercício 2 ---")
    l1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    l2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)
    print(l1)
    print(l2)

    print("\n--- Exercício 3 ---")
    print(f"Antes de emprestar: Disponível? {l1.disponivel}")
    l1.emprestar()
    print(f"Após emprestar: Disponível? {l1.disponivel}")
