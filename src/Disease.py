

class Disease():
    def __init__(self, name, contagiousness_rate, death_rate, infection_period, is_possible_immune ):
        self.is_possible_immune = is_possible_immune
        self.infection_period = infection_period
        self.death_rate = death_rate
        self.contagiousness_rate = contagiousness_rate
        self.name = name

