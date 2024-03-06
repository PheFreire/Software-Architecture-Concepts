import json

# Isso é uma interface que está definindo assinaturas usando o principio de segregação de interface
class Animal:
    def call(self, falar: str) -> str:
        raise NotImplementedError()
    
# Isso é um adaptador
class Gato(Animal):
    def call(self, falar: str) -> str:
        return " ".join(["miau" for _ in falar.split(" ")])

# Isso é um adaptador
class Chachorro(Animal):
    def call(self, falar: str) -> str:
        return " ".join(["auau" for _ in falar.split(" ")])
    
# Isso é um adaptador
class Pinto(Animal):
    def call(self, falar: str) -> str:
        return " ".join(["piupiu" for _ in falar.split(" ")])
    
# Isso é um adaptador
class Pato(Animal):
    def call(self, falar: str) -> str:
        return " ".join(["quack" for _ in falar.split(" ")])
    
# Isso é um fluxo recebendo uma interface como parametro usando os principios de:
    # Inversão de dependencia
    # Substituição de Liskov
def fluxo_de_falar(animal: Animal):
    print(animal.call("nicole maneira barbie gostoso"))


bridge = {
    "gato": Gato(),
    "chachorro": Chachorro(),
    "pinto": Pinto(),
    "pato": Pato(),
}

with open("./bridge.json") as j:
    dict_json = json.load(j)
    animal = bridge[dict_json["animal"]]
    fluxo_de_falar(animal)