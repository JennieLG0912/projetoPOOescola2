class Musica:
    def compositor(self):
        print("o compositor fez a musica: indiozinho")

class Receptor:
    def compositor(self):
        print("o fã escutou a musica: indiozinho ")

class Compositor:     
    def album(self):
        print("o compistor fez um album")           

class Albuns:
    def musica(self):
        print("as musicas que compoe esse album é: é voce e indiozinho  ")        

objetos = [Musica(), Receptor()]
for obj in objetos:
    obj.compositor()

objetos = [Compositor()]
for obj in objetos:
    obj.album()

objetos = [Albuns()]
for obj in objetos:
    obj.musica()