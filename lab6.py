# lab6.py
# Name: Hunter Monaghan
# I certify that this lab is my own work.
def sumList(nums):
        total = 0
        for i in nums:
                total += i
        return total

def squareEach(nums):
        square = 0
        for i in nums:
                square *= i
        return square
def toNumber(strings):
        line =[]
        line = ['21','04','32', '98','72']

        for element in strings:
                line.append(int(element))
        return line

def sumSquares(strings):
        #strings = ["7","3","6","1","10","2"]
        
        if(len(strings) == 0):
                return 0
        else:
                sums = (int)(strings[0])
                return (sums * sums) + sumSquares(strings[1:])
        strings = ["7","3","6","1","10","2"]
        answer = sumSquares(strings)

        print("The sum number of squares is: ", answer)

def sumSquaresFile(fileOutput):
        openFile = open("fileOutput.txt", "r")

        line = [(int)(i.strip()) for i in openFile.readlines()]
        sumSquare = 0

        for i in line:
                sumSquare = sumSquare + (i + i)
        return sumSquare

        file = input("Enter a fileName: ")
        answer = sumSquareFiles(fileOutput)
        print("The sum of the suares of numbers in the file is ", answer)

def applyRaises(wages,raises):
        fileOutput = open("outputFile.txt", "w")

        for line in wages:
                ls = line.split(" ")
                empid = ls[0]
                newWage = float(ls[3]) + float(ls[-1].rstrip("\n"))
                fileOutput.write(finalString)
                
def applyRaisesFile(employeeFile,outputFile):
        fileInput = open("employeeFile.txt", "r")
        wages = fileInput.readlines()
        applyRaises(wages,outputFile)

def main():
        #applyRaisesFile(inputFile,outputFile)
        #sumSquaresFile(fileOutput)
        #sumSquares(strings)
        #sumList(nums)
        #squareEach(nums)  
	#print("Testing sumList():")
	#print("[] ->", sumList([]))
	#print(sumList([5]))
	#print(sumList([10, 0.5]))
	#print(squareEach([]))
	#print(squareEach([5, 0.25, 2, 12, 6]))

##        toNumbers(strings)
	#print(toNumbers(strings))
        
        

        #if _name_=="_main_":
                #

        main()
        
