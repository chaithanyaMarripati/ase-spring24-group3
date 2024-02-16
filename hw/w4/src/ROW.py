import math
class ROW:
    def __init__(self, values):
        self.values = values 
    def d2h(self, data):
        distance = 0
        for col_index in data.cols['y']:  
            value = self.values[col_index]
        return distance 

# import math

# class ROW:
#     def __init__(self, values):
#         self.values = values

#     def d2h(self, data):
#         d, n = 0, 0
#         for col in data.cols['y']:
#             # print(col.heaven, col.norm(self.cells[col.at]))
#             print(data.cols)
#             n += 1
#             d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
#         return (d ** 0.5) / (n ** 0.5)

    # def d2h(self, data):
    #     distance = 0
    #     for col_index in data.cols['y']:
    #         # Assuming the optimal value ('heaven') for each column is stored in data.heaven[col_index]
    #         # You might need to adjust this based on how your 'heaven' values are stored
    #         optimal_value = data.heaven[col_index]
            
    #         # Ensure 'value' is a number before comparison
    #         try:
    #             value = float(self.values[col_index])
    #             # Calculate the squared difference between the value and its optimal value
    #             distance += (value - optimal_value) ** 2
    #         except ValueError:
    #             # Handle the case where 'value' cannot be converted to float (e.g., missing or non-numeric data)
    #             pass

    #     # Return the square root of the average squared difference
    #     # Adjust the calculation as needed based on your distance metric
    #     return math.sqrt(distance / len(data.cols['y'])) if data.cols['y'] else 0
