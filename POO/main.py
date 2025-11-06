from petshop import Adotante, Pet, Animal, Funcionario

adotante = Adotante()
pet = Pet()
animal = Animal(pet.tipo)

print(adotante.apresentar())
print(pet.apresentar1())
print(animal.apresentar())

# nao foi colocado na ordem dos demais pq essa parte fl funcionario é pra printar por ultimo, por isso é a confirmacao
funcionario = Funcionario(adotante, animal)
print(funcionario.apresentar())