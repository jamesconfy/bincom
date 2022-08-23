# A class for the project
class Bincom(object):
    # Initializing our given data and converting them to a key-pair datastructure (dictionary)
    def __init__(self, data):
        res = {}
        for col in data:
            if col in res:
                res[col] += 1
            else:
                res[col] = 1

        self.res = res

    # Method to get the most worn shirt
    def mostWorn(self):
        mostWorn = max(self.res.values())
        for keys, values in self.res.items():
            if values == mostWorn:
                return keys

    # Method to get the cummulative sum of values in the dataset
    def total(self):
        total = 0
        for _, values in self.res.items():
            total += values

        return total

    # Method to determine the mean of the dataset
    def mean(self):
        total = self.total()
        return total / len(self.res)

    # Method to determine the median of the dataset
    def median(self):
        total = self.total()
        return total / 2

    # Method to determine probability of getting a red shirt when drawn at random
    def probRed(self):
        countRed = self.res.get('RED')
        total = self.total()
        return countRed / total

    # Method to determine the variance of the dataset
    def variance(self):
        mean = self.mean()
        resultArr = []
        for _, value in self.res.items():
            squared = (value - mean) ** 2
            resultArr.append(squared)

        totalSum = sum(resultArr)
        variance = totalSum / len(self.res)
        return variance

    # Method on how to represent the data
    def __repr__(self):
        return f"Mean: {self.mean()} \nMost Worn: {self.mostWorn()} \nMedian: {self.median()} \nProbability of Getting a Red: {self.probRed()} \nVariance: {self.variance()}"
        

# Data gotten from the provided url (https://drive.google.com/file/d/1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf/view)
data = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",	
            "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",	
            "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
            "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
	


# Passing the data to the class and running each method
value = Bincom(data=data)
print(repr(value))