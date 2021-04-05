class Health:
    def __init__(self, health1, health2, listaPokemon):
        self.health1 = health1
        self.health2 = health2
        self.listaPokemon = listaPokemon
    
    def health1_decay(self, damage_taken):
        self.health1 -= damage_taken
        return self.health1
    
    def health2_decay(self, damage_taken):
        self.health2 -= damage_taken
        return self.health2
