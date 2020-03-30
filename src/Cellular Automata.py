from .Interfaces import CAInterface


class CellularAutomata(CAInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compute_step(self):
        raise NotImplementedError
