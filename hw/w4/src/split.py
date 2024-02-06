class DATA:

    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols['names'])
        maximum = float('inf')
        out = 1

        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)
            
            tmp = abs(b + r) / abs(b - r + 1E-300)
            if tmp < maximum:  
                out, maximum = i, tmp

        return out, selected 
