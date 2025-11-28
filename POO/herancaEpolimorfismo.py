class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def acao(self):
        print(f"{self.nome} está fazendo algo...")

class Compositor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.musicas_compostas = []

    def compor_musica(self, titulo, duracao):
        musica = Musica(titulo, duracao, self)
        self.musicas_compostas.append(musica)
        print(f" {self.nome} compôs a música '{titulo}'.")
        return musica

    def criar_album(self, titulo, musicas):
        album = Album(titulo, musicas)
        print(f" {self.nome} criou o álbum '{titulo}'.")
        return album

    def acao(self):
        print(f" Compositor {self.nome} está criando novas músicas...")


class Receptor(Pessoa):
    def acao(self):
        print(f" Fã {self.nome} está ouvindo suas músicas favoritas.")

    def escutar(self, musica):
        print(f" {self.nome} está escutando '{musica.titulo}' ({musica.duracao} min).")


class Musica:
    def __init__(self, titulo, duracao, compositor):
        self.titulo = titulo
        self.duracao = duracao
        self.compositor = compositor

    def detalhes(self):
        print(f" - '{self.titulo}' ({self.duracao} min), composta por {self.compositor.nome}")


class Album:
    def __init__(self, titulo, musicas=None):
        self.titulo = titulo
        self.musicas = musicas if musicas else []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def mostrar_album(self):
        print(f"\n Álbum: {self.titulo}")
        for musica in self.musicas:
            musica.detalhes()

comp = Compositor("Carlos")
fa = Receptor("Ana")

pessoas = [comp, fa]
for pessoa in pessoas:
    pessoa.acao()

m1 = comp.compor_musica("Índiozinho", 3.2)
m2 = comp.compor_musica("É Você", 2.8)
m3 = comp.compor_musica("Caminho da Tribo", 4.1)

album = comp.criar_album("Coleção Tribal", [m1, m2, m3])

album.mostrar_album()

fa.escutar(m1)
fa.escutar(m3)