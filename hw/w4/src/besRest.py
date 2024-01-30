class DATA:
    def bestRest(self, rows, want, best, rest, top):
        rows.sort(key=lambda row: row.d2h(self))
        best, rest = [self.cols.names], [self.cols.names]

        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)

        return DATA.new(best), DATA.new(rest)
