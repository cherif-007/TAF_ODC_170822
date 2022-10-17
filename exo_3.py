class Personne:
    def __init__(self, nom = 'Joshua', prenom='Moses', cin='096/btf'):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
    
    def __str__(self):
        return self.prenom + " " + self.nom + " " + self.cin

p1 = Personne()

class Vaccine(Personne):
    def __init__(self, code_vaccine, date_vaccine):
        Personne.__init__(self, nom='', prenom='', cin='')
        self.code_vaccine = code_vaccine
        self.date_vaccine = date_vaccine

    def get_code_vaccine(self):
        return self.code_vaccine

    def set_code_vaccine(self):
        self.code_vaccine = self.code_vaccine

    def get_date_vaccine(self):
        return self.date_vaccine

    def set_date_vaccine(self):
        self.date_vaccine = self.date_vaccine

    def __str__(self):
        return p1.prenom + " " + p1.nom + " code " + self.code_vaccine + " vaccine le " + self.date_vaccine

v1 = Vaccine('22','17-10-2022')
print(v1)

class Vaccin:
    def __init__(self, code_vaccin, nom_vaccin, duree_entre_doses):
        self.code_vaccin = code_vaccin
        self.nom_vaccin = nom_vaccin
        self.duree_entre_dose = duree_entre_doses

    def __str__(self) -> str:
        return self.code_vaccin + " " + self.nom_vaccin + " " + self.duree_entre_dose

vaccin1 = Vaccin('1', 'flutt', '2')
print(vaccin1)
        