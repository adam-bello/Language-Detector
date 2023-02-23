import string
import numpy as np
import sys

def main(inputFile, outputFile) :
    langDict = initDictionary()
    unknown = {}
    file = open(inputFile)
    Lines = file.readlines()
    # Read through each line of the file
    for line in Lines :
        # Split each line into the language and the file name
        curLine = line.split()
        if (len(curLine) == 2) :
            cleanDoc = clean(curLine[1])
            vector = countTrigrams(cleanDoc)
            # If the document is a language, update the corresponding vector
            # in the language dictionary
            if (curLine[0] != "Unknown") :
                langDict[curLine[0]] = updateVector(langDict[curLine[0]], vector)
                # If the document is unknown add it to the unknown dictionary with
                # its corresponding vector
            elif (curLine[0] == "Unknown") :
                unknown[curLine[1]] = vector
    # Normalize all the vectors in the language dictionary
    for v in langDict.values() :
        v = normalizeVector(v)
    writeOutput(unknown, langDict, outputFile)
    return

# Write the output to a file as a list of unknown files and their 
# similarity metric for each language
def writeOutput(unknownFiles, langDict, outputFile) :
    f = open(outputFile, "w")
    for testFile in unknownFiles :
        f.write(testFile + "\n")
        for v in langDict.keys() :
            output = compareVectors(unknownFiles[testFile], langDict[v])
            f.write(v + ": ")
            f.write(str(output) + "\n")
        f.write("\n")
    f.close()
    return

# Normalize a vector by dividing each trigram frequency by the total
# number of the trigrams
def normalizeVector(vector) :
    count = 0.0
    for value in vector :
        count += value
    vector = [num / count for num in vector]
    return vector

# Add a new vector to an old vector by adding corresponding elements
def updateVector(old, new) :
    for i in range(len(old)) :
        old[i] = old[i] + new[i]
    return old
        
# Initialize the language dictionary with the languages we are using
def initDictionary() :
    langDict = {}
    langDict["Croatian"] = initVec()
    langDict["Dutch"] = initVec()
    langDict["English"] = initVec()
    langDict["French"] = initVec()
    langDict["German"] = initVec()
    langDict["Romanian"] = initVec()
    langDict["Spanish"] = initVec()
    return langDict
        
# Clean a file of punctuation, capitals, numbers, etc.
def clean(filename) :
    result = ""
    file = open(filename)
    for line in file :

        line = ''.join(i for i in line if not i.isdigit())
        line = ''.join(i for i in line if i not in string.punctuation)
        line = line.strip()
        line = line.lower()
        result = result + line
    return result

# Count the trigrams in a given document
def countTrigrams(doc) :
    count = 0.0
    resultList = initVec()
    for i in range(len(doc) - 2) :
        count += 1.0
        trigram = doc[i] + doc[i+1] + doc[i+2]
        resultList[findIndex(trigram)] += 1.0
    resultVector = np.array(resultList)
    return resultVector

# Use the cosine similarity formula to compare 2 vectors
def compareVectors(vector1, vector2) :
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    val = np.dot(vector1, vector2) / (norm1 * norm2)
    return val

# Initialize a vector for all possible trigrams to values of 0 at each index
def initVec() :
    initVector = []
    for i in range(27**3) :
        initVector.append(0)
    return initVector

# Find the correct index of a given trigram 
# sorted '   ', '  a', '  b' ... ' a ', ' aa' ... 'zzz'
def findIndex(trigram) :
    index = 0
    place = 2
    for c in trigram :
        if (c == ' ') :
            index = index + (0 * 27**place)
        elif (c == 'a') :
            index = index + (1 * 27**place)
        elif (c == 'b') :
            index = index + (2 * 27**place)
        elif (c == 'c') :
            index = index + (3 * 27**place)
        elif (c == 'd') :
            index = index + (4 * 27**place)
        elif (c == 'e') :
            index = index + (5 * 27**place)
        elif (c == 'f') :
            index = index + (6 * 27**place)
        elif (c == 'g') :
            index = index + (7 * 27**place)
        elif (c == 'h') :
            index = index + (8 * 27**place)
        elif (c == 'i') :
            index = index + (9 * 27**place)
        elif (c == 'j') :
            index = index + (10 * 27**place)
        elif (c == 'k') :
            index = index + (11 * 27**place)
        elif (c == 'l') :
            index = index + (12 * 27**place)
        elif (c == 'm') :
            index = index + (13 * 27**place)
        elif (c == 'n') :
            index = index + (14 * 27**place)
        elif (c == 'o') :
            index = index + (15 * 27**place)            
        elif (c == 'p') :
            index = index + (16 * 27**place)
        elif (c == 'q') :
            index = index + (17 * 27**place)
        elif (c == 'r') :
            index = index + (18 * 27**place)
        elif (c == 's') :
            index = index + (19 * 27**place)
        elif (c == 't') :
            index = index + (20 * 27**place)            
        elif (c == 'u') :
            index = index + (21 * 27**place)
        elif (c == 'v') :
            index = index + (22 * 27**place)
        elif (c == 'w') :
            index = index + (23 * 27**place)
        elif (c == 'x') :
            index = index + (24 * 27**place)
        elif (c == 'y') :
            index = index + (25 * 27**place)
        elif (c == 'z') :
            index = index + (26 * 27**place)
        place = place - 1
    return index

# For running the program from the command line
if (len(sys.argv) == 3) :
    main(sys.argv[1], sys.argv[2])