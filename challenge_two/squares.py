class Squares:
    def compute_squares(self):
        dictionary = {}
        for number in range(1,16):
            number_square = number*number
            dictionary[number] = number_square
            print(dictionary)
            dictionary.clear()
squares_instance = Squares()
squares_instance.compute_squares()