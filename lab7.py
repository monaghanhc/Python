## lab7.py
## Name: Hunter Monaghan

from graphics import *
import math

def isTeen(num):
        if num >= 13 and num <= 19:
                print("true, your number is between 13 and 19")
        else:
                print("False, your number is beyond the perimeter of 13 through 19")
def isOdd(num):
        if (num % 2)==0:
                print("False, Its Even")
        else:
                print("True, Its Odd")
def classRank(credits):
        
        
       # credit = int(input("Enter in the amount of credits: "))
                
       # if credit >= 90:
      #          print("You are a Senior " )
     #   elif credit <= 89 and credit >= 60:
    #            print("You are a Junior ")
   #     elif credit <= 59 and credit >= 30:
  #              print("You are a Sophomore ")
#        elif credit <= 29:
#                print("You are a Freshman ")
#         else:
#                 print("NA")

#This one is the assingment below but the I like using the input function more, feel like its more-
#user friendly, above.
        if credits >= 90:
                print("You are a Senior " )
        elif credits <= 89 and credits >= 60:
                print("You are a Junior ")
        elif credits <= 59 and credits >= 30:
                print("You are a Sophomore ")
        elif credits <= 29:
                print("You are a Freshman ")
        else:
                print("NA")

        #print("Your have", credits + "credits")    
                #SystemExit
                #copyright

        
def starter(weight, wins):
        if weight >= 150 and weight < 160 and wins >= 5:
                print("Qualified!")
                return True # tried without returning and still works
        elif weight > 199 or wins > 20:
                print("Qualified")
                return True
        else:
                print("Unqualified")
                return False


#Look into return more
def isLeapYear(year):
        #year = 365.2422
        if year % 4 == 0:
                if year % 400 == 0:
               #        print("{0} is a leap year ")
                        if year % 100 == 0:
                                print("{0} is a leap year".format(year))
                        else:
                                print("{0} is not a leap year".format(year))
                else:
                        print("{0} is a leap year".format(year))
        else:
                print("{0} is not a leap year".format(year))

                
def distance(pointX1, pointY1, pointX2, pointY2):
        yInt = pointY2 - pointY1
        xInt = pointX2 - pointX1
        total = (xInt ** 2)+(yInt ** 2)
        distance = math.sqrt(total)
        return distance

        

        #area = math.sqrt(distance/pi) 
        #radius = d/2
        #d = circum / pi
        #circum = d*pi  or  2*pi*r
        
#def overlap():
def overlap(pointX1, pointY1, pointX2, pointY2):
        
    # Draw two circles and determine whether they overlap.
    #NEED TO MAKE A 2nd CIRCLE
        #circle2 = Circle(pointX2, pointY2, 50)
        #circ2 = Circle(pointX1, pointY1, 50)

        
    # Build window
        winHeight = 400
        winWidth = 400
        win = GraphWin("Overlapping circles", winHeight, winWidth)

    # Text area for instructions for user
        instruct = Text(Point(winWidth/2, winHeight-10), "")
        instruct.draw(win)

    # Get center point and x/y for center
        instruct.setText("To draw a circle, click the centerpoint for the circle")
        center = win.getMouse()
        center.draw(win)

    # Get point on the circumference and its x/y coordinates
        instruct.setText("Click a point on the border of the circle.")
        border = win.getMouse()

    #Calculate radius using Euclidean distance
        radius = distance(pointX2, pointY2)
        circle = Circle(pointX2, pointY2)
        circle.draw(win)
        #circ2.draw(win)

    # Wait for another click to exit
        instruct.setText("Click anywhere to close.")
        win.getMouse()
        win.close()

def isValid(isbn):
        pass
        
        

def main():
        #isTeen(10)
        #isOdd(22)
        #isOdd(21)

        #starter(155, 6)
        #starter(180, 19)
        #starter(200, 0)

        #isLeapYear(2004)#Not a leap year
        #isLeapYear(2001)# Is a Leap yar 
        #print(year + "is a leap year")
        #print(year + "is not a leap year")

       # distance(pointX1, pointY1, pointX2, pointY2)
        print(distance(3,4,6,8))
        print(distance(10,12,1,2))
        distance(pointX1, pointY1, pointX2, pointY2)
        overlap()
        #overlap(pointX1, pointY1, pointX2, pointY2)

        #classRank(credits) #input with class rank
        #classRank(24) #original assingment
        
    # Add code to test the indicated functions
	#pass
main()
