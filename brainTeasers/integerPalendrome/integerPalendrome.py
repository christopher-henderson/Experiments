def isPalendrome(forwards):
    return forwards == forwards[-1::-1]
 
def getNextPalendrome(number):
    stringNumber = str(number)
    if isPalendrome(stringNumber):
        result = number + 1
    else:
        result = number
    
    upperOrderOfMagnitude = len(stringNumber) - 1
    lowerOrderOfMagnitude = 1
    
    
    while lowerOrderOfMagnitude <= upperOrderOfMagnitude:
        rightDigit = (result % 10**lowerOrderOfMagnitude) // (10**(lowerOrderOfMagnitude - 1))
        leftDigit = (result // 10**upperOrderOfMagnitude) % 10
        difference = leftDigit - rightDigit
        #print (result, leftDigit,rightDigit)
        if difference < 0:
            difference += 10
        result += difference*10**(lowerOrderOfMagnitude-1)
        lowerOrderOfMagnitude += 1
        upperOrderOfMagnitude -= 1
    return result

print (getNextPalendrome(9864643541368163513))