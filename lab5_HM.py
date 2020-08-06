# lab5.py
# Name:Hunter Monaghan
# Certify that this is my own work

# Examples of splitting strings
def splitStrings():
	# default usage (no delimeter specified)
	sentence = input("Enter a sentence to see how split() works: ")
	print("Result of sentence.split():", sentence.split())
	
	# splitting on a delimiter
	values = input("Enter a sequence of values separated by commas: ")
	print("Result of values.split():", values.split(", "))
pass

# Convert a sentence to UPPERCASE.
def allCaps():
        lowerCase = print("Enter in a sentence: ")
        upperCase = input()
        print(upperCase.upper())
        print()

def search():
        #sentence
        sentence = print("Enter the a sentence: ")
        outputS = input()
        print(outputS)
        print()
        #word
        word = print("Enter in a word you want to be searched: ")
        outputW = input()
        #output
        print(outputS.find(outputW)+1)
        print()



def companyName():
        domain = input('Enter in a domain name : ')

        word = domain.split('.')[1]
        string = ''
        for i in range(len(word)):
                if i==0:
                        string = string + word[i].upper()
                else:
                        string = string + word[i]
        print(string)
        print()

def nameReverse(firstName, lastName):
        first = firstName
        last = lastName

        print("Your name is " + 1 + " " + first)
        return
        print()

def thirds(): 
        List = []
        n = int(input("Enter number of elements: "))
        
        for i in range(0, n):
                ele = input()
                List.append(ele)
                
        for i in range(0,n):
                str = List[i]
                res = ""
        for index, char in enumerate(str):
                if index%3==2 :
                        res+=char
        print(res)
        print()
        
                
        

def wordAverage():
        print("Word Average")
        print()
        sentence = input("Enter a sentence: ")
        word = sentence.split()
        average = (sum(map(len, word)) / len(word))
        print()
        print("Average is: ")
        print(round(average, 1))
        print()

def names():
        
        fullName = input("Enter your friend's names, separated by a comma: ");
        #splitting
        fullName_list = fullName.split(', ')
        #Output
        print("The initials are", end=" ")

        
        for i in fullName_list:
                #splitting each into an array 
                ans = i.split(" ")
                print(ans[0][0] + ans[1][0],end=" ")
                print()

def pigLatin():
        
        firstSentence = input("Enter the sentence: ")
        words = firstSentence.split()
        secondSentence = ""
        for i in words:
                secondSentence = secondSentence + i[1:] + i[0] + "ay "
                secondSentence = secondSentence.capitalize()
                secondSentence = secondSentence.lower()
  
        return secondSentence

        print(pigLatin())
        print()

def addOne():
        #Input
        myString =  input("Enter list of numbers with seperating it with a comma: ")
        nums = myString.split(",")
        for i in range(0, len(nums)):
                #Logic
                nums[i] = float(nums[i]) + 1
        answer = ", ".join([str(number)for number in nums])
        print()
        #Output
        print("Updated List: ", answer)
        print()
def encode():
        encodedText = input("enter the text you'd like to encode: ")
        key = int(input("Enter an integer to act as the key:  "))

        encodedAnswer = ""
        for character in encodedText:
                encodedAnswer = encodedAnswer + chr(ord(character) + key)
        print()
        print("Your encoded message reads: ")
        print(encodedAnswer)

        decodedAnswer = ""
        for character in encodedAnswer:
                decodedAnswer = decodedAnswer + chr(ord(character) - key)
        print()
        print("Your decoded message reads: ")
        print(decodedAnswer)
                        
def main():
        
        allCaps()
        search()
        #splitStrings()
        companyName()
        nameReverse(firstName, lastName)
        #thirds()
        wordAverage()
        names()
        pigLatin()
        addOne()
        encode()
    # You can add the other function calls here
	
	
main()
