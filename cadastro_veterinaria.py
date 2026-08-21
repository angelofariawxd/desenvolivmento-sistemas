class Veiculo:
    def calcular_custo(self, distancia):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses")

class Carro(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.8  # Exemplo: custo de R$0,50 por km

class Bicicleta(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.28  # Exemplo: custo de R$0,10 por km

class Caminhao(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 1.32  # Exemplo: custo de R$1,00 por km

# Uso do polimorfismo
veiculos = [Carro(), Bicicleta(), Caminhao()]
distancia = 100  # Exemplo de distância

for veiculo in veiculos:
    custo = veiculo.calcular_custo(distancia)
    print(f"Custo de viagem com {veiculo.__class__.__name__}: R${custo}")

class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        pass  # Será sobrescrito nas classes filhas


class Cachorro(Animal):

    def emitir_som(self):
        return "Au Au!"


class Gato(Animal):

    def emitir_som(self):
        return "Miau!"


class ClinicaVeterinaria:

    def __init__(self):
        self.pacientes = []

    def cadastrar(self, animal):
        self.pacientes.append(animal)

    def listar_atendimentos(self):
        print("--- PACIENTES CADASTRADOS ---")
        for animal in self.pacientes:
            # Polimorfismo: o método emitir_som() se adapta de acordo com a classe do objeto
            print(
                f"Nome: {animal.nome} | Idade: {animal.idade} anos | Som: {animal.emitir_som()}"
            )


# --- Testando o sistema ---
clinica = ClinicaVeterinaria()

# Criando diferentes tipos de animais
dog = Cachorro("Rex", 3)
cat = Gato("Mimi", 2)

# Cadastrando os animais
clinica.cadastrar(dog)
clinica.cadastrar(cat)

# Exibindo os cadastros
clinica.listar_atendimentos()
