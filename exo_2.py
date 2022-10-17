class Pet():
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animalType = animalType
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_animalType(self):
        return self.__animalType

    def set_animalType(self, animalType):
        self.__animalType = animalType

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
    
    def saisir_infos(self):
        self.set_name(input('Entrer le nom: '))
        self.set_animalType(input('Entrer le type: '))
        self.set_age(int(input('Entrer l\'age: ')))

    def recuperer_infos(self):
        self.get_name()
        self.get_animalType()
        self.get_age()

    def afficher_infos(self):
        print('L\'animal se nomme: {} ; il est de type : {} et il a : {} ans'.format(self.__name, self.__animalType, self.__age))

pet = Pet('', '', '')
pet.saisir_infos()
pet.afficher_infos()