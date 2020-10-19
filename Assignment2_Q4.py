# The Author of this python script is Smit Panchal B00828070

'''
BitsStuffing() is a method which will accept a parameter of String type i.e. the name of the file.
The below method will take a txt file which will contain text. Next, all the characters in the
file will get converted into it's equivalent ASCII value and then it will be converted to binary
number. Lastly, it will append 0 after every 5 consecutive 1s and will write it to the file.
I have performed all the operations on list.
'''
def BitsStuffing(FileName = ""):
    print("---------------------------------------------------------------------------------------------------------")
    print("Method BitsStuffing() is called which will convert Text to stuffed binary values")
    print("---------------------------------------------------------------------------------------------------------")

    # Open and read the file which is provided in the parameter.
    myFile = open(FileName, "r")
    text = myFile.read()

    # A temporary empty list which contain binary numbers
    finalBinaryValueList = []

    # Looping through the content in the txt file
    for t in text:
        # finalList will contain the stuffed binary numbers.
        finalList = []

        # ord() method will convert the characters to its ASCII values.
        myAscii = ord(t)
        # bin() method will convert the ASCII value to its binary value.
        myBin = bin(myAscii)
        # Slicing the binary value as the starting 2 characters is same and does not count.
        finalBinaryValue = myBin[2:]
        # Finally appending it to the list by converting it into int.
        finalBinaryValueList.append(int(finalBinaryValue))

        # Below is the logic to append 0 after 5 consecutive 1s
        for f in finalBinaryValueList:
            if ('11111' in str(f)):
                finalValue = str(f).replace('11111', '111110')
                finalList.append(int(finalValue))
            else:
                finalList.append(int(f))
    print("Below is the list of Binary Values without bit stuffing: ")
    print(finalBinaryValueList,'\n')
    print("Below is the list of Binary Values with bit stuffing: ")
    print(finalList,'\n')

    # Providing the name of the file
    filename = "BitsStuffingFile" + ".txt"
    # Opening the file in write mode and converting list data into string.
    f = open(filename, "w")
    # Writing the list content to file
    f.write(str(finalList))
    return finalList

'''
BitsToString() is a method which will accept a parameter i.e. the bits stuffed values.
The below method will first remove the 0 which was earlier stuffed. Next, it will convert
the values into ASCII values and finally into String.
I have performed all the operations on list.
'''
def BitsToString(inBits):
    finalString = ""
    unPadBinaryList = []
    print("---------------------------------------------------------------------------------------------------------")
    print("Method BitsToString() is called which will convert stuffed binary values into Text")
    print("---------------------------------------------------------------------------------------------------------")

    print("Below is the list of Binary Values with bit stuffing: ")
    print(inBits,'\n')

    # Logic to remove the stuffed 0 from the binary values and stored in the list.
    for b in inBits:
        if ('111110' in str(b)):
            unPadValue = str(b).replace('111110', '11111')
            unPadBinaryList.append(str(unPadValue))
        else:
            unPadBinaryList.append(str(b))
    print("Below is the list of Removed Stuffed Bit stream")
    print(unPadBinaryList,'\n')
    # Looping through the values and converting to characters.
    for i in unPadBinaryList:
        # Converting the binary values to int base 2 decimal
        baseVal = int(i, 2)
        # chr() will convert the int values to ASCII characters
        asciiChar = chr(baseVal)
        # Adding ASCII characters together
        finalString = finalString + asciiChar

    # Providing the name of the txt file
    filename = "TextFile(BitsToTextFile)" + ".txt"
    # Opening the file in write mode and converting list data into string.
    f = open(filename, "w")
    # Writing the string values to file.
    f.write(str(finalString))
    return finalString

userInput = input("Please Enter the file name with file extension as txt: ")
# Calling the methods which will return stuffed bits by passing the parameters and store it to variable.
inBits = BitsStuffing(userInput)
# Calling the methods which will return text by passing the parameters and store it to variable.
inString = BitsToString(inBits)
print("Below is the text that we provided in file which is converted back from binary to text: ")
print(inString)
