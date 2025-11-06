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
        print(" as musicas que compoe esse album é: é voce e indiozinho  ")        

def fazer_compositor(obj):
    obj.compositor()

def fazer_album(obj):
    obj.album()    


def fazer_musica(obj):
    obj.musica()

m = Musica()
r = Receptor()
c = Compositor()
a = Albuns()

fazer_compositor(m)
fazer_compositor(r)
fazer_album(c)
fazer_musica(a)

objetos = [Musica(), Receptor()]

for obj in objetos:
    obj.compositor()
