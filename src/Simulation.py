from .Interfaces import SimulationInterface


class Simulation(SimulationInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def simulate(self):
        raise NotImplementedError
