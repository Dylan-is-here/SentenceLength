import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    # print(words)

    sentences = textInFile.split(".")
    delimiters = delimiters.split()
    #For every delimiter (symbol) loop through
    for i in range(len(delimiters)):
        delimiter = delimiters[i] #go through one delimiter at a time
        if len(delimiters) > 0: #make sure there is delimiters
            for j in range(len(sentences)):
                if delimiter in sentences[j]: #go through each sentence and check if it contains the delimiter
                    additionalSentences = (sentences[j].split(str(delimiter)))
                    for sentence in additionalSentences: 
                        sentences.append(sentence) 
                        #Takes the split sentence which starts as a list(1 item) and turns it into 
                        #two list elements in sentences(two list items)
                        #Ex: ["other sentence.", ["blah blah? yes."]](counts as 2 length)
                        #Turns into ["other sentence.", "blah blah", "yes."]](3 length for more accurate calculation)
                    sentences.remove(sentences[j])#fixes sentence number

    sentences.remove("")

    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return int(round(aveSentenceLength, 0))


def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze.\n")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence delimiters separated by spaces.\n")
    minLength = input("Enter the minimum length of a word (must be a positive integer).\n")
    
    minLenPro = ""

    for i in range(len(minLength)):
        # print("1234567890".contains(minLength[i]))
        if (minLength[i] in "1234567890") == False:
            minLenPro = minLenPro + ""
        else:
            minLenPro = minLenPro + minLength[i]
    if minLenPro == "":
        minLenPro = 3
        mlp = int(minLenPro)
        
    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, mlp))

if __name__ == "__main__":
    main()
