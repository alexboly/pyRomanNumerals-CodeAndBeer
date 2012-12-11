from unittest import TestCase
import random

def convertRomanNumerals(romanNumerals):
    value = 0
    reversedRomanNumber = romanNumerals[::-1]
    previousValue = getValueForSymbol(reversedRomanNumber[0])
    
    for romanSymbol in reversedRomanNumber:
        currentValue = getValueForSymbol(romanSymbol)
        isAddition = previousValue <= currentValue
        sign = 1 if isAddition else -1
        value += sign * currentValue
        previousValue = currentValue if isAddition else previousValue
        
    return value

def getValueForSymbol(romanSymbol):
    return {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                    }[romanSymbol]

def main():
    latinQuotes = [
                   'Alea jacta est',
                   'Acvila non capit muscam',
                   'Veni, vidi, vici',
                   'aut viam inveniam aut faciam'
                   ]
    quoteIndex = random.randint(0, len(latinQuotes))
    
    print "Input a roman number:"
    romanNumber = raw_input(latinQuotes[quoteIndex] + ' > ')
    print "It means: ", convertRomanNumerals(romanNumber)
    
if(__name__ == "__main__"):
    main()

class RomanNumeralsTest(TestCase):

    valuesDictionary = {"I" : 1,
                        "II": 2,
                        "III" : 3,
                        "VI" : 6,
                        "VII" : 7,
                        "XIII" : 13,
                        "LIII": 53,
                        "CXXX" : 130,
                        "DXXX" : 530,
                        "IV" : 4,
                        "CM" : 900,
                        "CMX" : 910,
                        "MCMLIV" : 1954,
                        "CCM" : 800,
                        "MCCM" : 1800,
                        "MCCMXXL": 1830,
                        "CCCCCM" : 500,
                        "IIIIIV" : 0
                        }
    
    def testValues(self):
        actual = map(convertRomanNumerals, self.valuesDictionary.keys())
        
        self.assertEquals(actual, self.valuesDictionary.values())
