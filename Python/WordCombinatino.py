def Process(originals, pointWords, result):
    withoutPoints = [w for w in originals if w not in pointWords]
    
    for wp in withoutPoints:
        clonePointWords = pointWords[:]
        clonePointWords.append(wp)
        result.append(clonePointWords)
        Process(originals, clonePointWords, result)

def Start(listOfWords):
    result = []

    for w in listOfWords:
        Process(listOfWords, [w], result)

    for r in result:
        print (r)


Start(['A','B','C']);

