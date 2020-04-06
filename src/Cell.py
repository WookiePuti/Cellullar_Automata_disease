from Interfaces import CellInterface
import enum


class CellStatus(enum.Enum):
    susceptible = 1
    infected = 1
    dead = 3
    recovered = 4


class CellDisease(CellInterface): #single cell representing some area of country or oneperson
    def __init__(self, x_coord, y_coord, cell_status: CellStatus,   *args, **kwargs):
        self.cell_status = cell_status
        self.illness_counter = 0
        super().__init__(x_coord, y_coord, *args, **kwargs)

    def perform_state_transition(self):
        raise NotImplementedError


