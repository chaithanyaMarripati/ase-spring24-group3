from SYM import SYM
from NUM import NUM


class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = {}, {}, []
        self.klass, col = None, None
        for at, txt in enumerate(row.cells):
            col = (NUM if txt[0].isupper() else SYM)(
                txt, at
            )  # Instantiate NUM or SYM directly
            self.all.append(col)
            # this is guard statement for the txt ending with X
            if txt.endswith("X"):
                continue

            # if txt ends with !, it should be the final class of the row
            if txt.endswith("!"):
                self.klass = col
            # if txt ends with these, it will be y class
            if txt.endswith(("!", "+", "-")):
                self.y[at] = col
            else:
                self.x[at] = col
        self.names = row.cells

    def add(self, row):
        # add new data to cols
        for cols in [self.x.values(), self.y.values()]:
            for col in cols:
                col.add(row.cells[col.at])
        return row
