# Exercice de POO:
# Créer une base de données en dictionnaire plus proche de ce que serait une véritable base de données.
# le dictionnaire databases doit:
# - avoir des clés sous forme d'integer (ce seront les IDentifiants)
# - avoir en valeur: une list de chaines de caractères, avec dans l'ordre: username, first_name, email, password

# Définir une class User avec
# - les attributs d'instance: username, first_name, email, password, id
# - une méthode __str__ pour mieux lire l'instance
# - une méthode save pour sauvegarder l'objet en base de données, on utilisera l'attribut 'id' pour savoir où sauvegarder les données

# - une méthode "create" pour créer un nouvel objet User en base de données, qui attendra tous les attribut cités plus haut sauf 'id'
#   car l'ID sera automatiquement généré lors de la création (dans la méthode create)

# - une méthode de classe 'get' pour récupérer l'objet:
#   - on attendra l'ID pour savoir où récupérer l'objet
#   - une fois qu'on a récupéré les données, on instanciera la classe User avec les données, et on retournera l'instance




database = {
    1: ["pedro", "Pierre", "pierre@expl.fr", "123"],
    2: ["polo", "Paul", "paul@expl.fr", "456"],
    3: ["jaco", "Jacques", "jacques@expl.fr", "789"]
}



class User:

    def __init__(self, username, firstname, email, password):
        self.username = username
        self.firstname = firstname
        self.email = email
        self.password = password
        self.id = None
        

    def __str__(self):
        return f"{self.username} - {self.firstname} - {self.email} - {self.password}"
    
    def save(self):
        is_update = self.id is not None
        if is_update:
            database[self.id] = [self.username, self.firstname, self.email, self.password]
        else:
            id = len(database) + 1
            self.id = id
            database[self.id] = [self.username, self.firstname, self.email, self.password]
            
        


    @classmethod
    def get_from_database(cls, id: int):
        """Get a user from the database."""
        data = database[id]
        username, first_name, email, password = data
        user = User(username, first_name, email, password)
        user.id = id
        return user




my_user = User.get_from_database(2)

print(my_user)

breakpoint()

