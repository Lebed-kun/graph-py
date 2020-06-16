class Math:
    @staticmethod
    def safeMin(number1, number2):
        if number1 is None:
            return number2
        elif number2 is None:
            return number1
        else:
            return number1 if number1 < number2 else number2
    
    @staticmethod
    def safeMax(number1, number2):
        if number1 is None:
            return number2
        elif number2 is None:
            return number1
        else:
            return number1 if number1 > number2 else number2

class Set:
    @staticmethod
    def product(set1, set2):
        result = set()

        for el1 in set1:
            for el2 in set2:
                result.add((el1, el2))
        
        return result