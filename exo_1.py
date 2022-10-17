class Table:
    def __init__(self, reference, matiere, poids, hauteur, longueur, largeur, prix_vente, prix_fabrication, nb_table_stock):
        self.reference = reference
        self.matiere = matiere
        self.poids = poids
        self.hauteur = hauteur
        self.longueur = longueur
        self.largeur = largeur
        self.prix_vente = prix_vente

        self.__prix_fabrication = prix_fabrication
        self.__nb_table_stock = nb_table_stock

    def get_prix_fabrication(self):
        return self.__prix_fabrication

    def set_prix_fabrication(self, prix_fabrication):
        self.__prix_fabrication = prix_fabrication

    def get_nb_table_stock(self):
        return self.__nb_table_stock

    def set_nb_table_stock(self, nb_table_stock):
        self.__nb_table_stock = nb_table_stock

    def affiche_table(self):
        print('La reference de la table est: {}\n La matiere est: {}\n La longeur fait : {} cm\n La largeur fait: {} cm\n La hauteur fait: {} cm\n Le poids fait: {} \n Le prix de vente est: {} '.format(self.reference, self.matiere, self.longueur, self.largeur, self.hauteur, self.poids, self.prix_vente))

    def calcul_gain(self):
        gain = ((self.prix_vente - self.get_prix_fabrication()) * self.get_nb_table_stock())
        print('Le gain suivant le nombre de stock est : ', gain)

t1 = Table(reference='T-001', matiere='bois_rouge', poids=12, hauteur=50, longueur=20, largeur=20, prix_vente=4000, nb_table_stock=43, prix_fabrication=3000)
print('<<< INFORMATION SUR LA TABLE >>>')
t1.affiche_table()
print('<<< CALCUL DE GAIN PREVU >>>')
t1.calcul_gain()