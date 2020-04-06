from abc import abstractmethod, ABC


class CellInterface(ABC):
    def __init__(self, x_coord, y_coord, *args, **kwargs):
        self.x_coord = x_coord
        self.y_coord = y_coord
        super().__init__(*args, **kwargs)

    @abstractmethod
    def perform_state_transition(self):
        pass


class CAInterface(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def compute_step(self):
        pass


class SimulationInterface(ABC):
    @abstractmethod
    def simulate(self):
        pass








class Miod:
    def __init__(self, b):
        self.b = b


class Mleko:
    def __init__(self, a):
        self.a = a


