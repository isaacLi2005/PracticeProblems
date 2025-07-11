def main():
    inputString = input()

    lettersDict = dict()
    for i in range(len(inputString)):
        if inputString[i] not in lettersDict:
            lettersDict[inputString[i]] = 1
        else:
            lettersDict[inputString[i]] += 1
    
    resultL = []
    for i in range(len(inputString)):
        

pass