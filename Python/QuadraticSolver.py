
#Angus Munro 
#Quadratic Solver
#October 3 

#start up message
print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")

#gets inputs from user
a = input("A Value: ")
b = input("B Value: ")
c = input("C Value: ")

#adds inputs to inputArray
inputArray = [int(a),int(b), int(c)]

#creates empty root array
rootArray = []

#main function
def discrimFunc(vals):
	
	#easier to write the equations with aa instead of vals[0]
	aa = vals[0]
	bb = vals[1]
	cc = vals[2]
	
	#tests for real roots
	if bb*bb - 4*aa*cc < 0:
		
		#rootArray becomes No Real roots
		rootArray.append("No Real")
		rootArray.append("Roots")
	else:
		
		#finds the roots via quadratic formula
		rootA =(-bb + (bb*bb-4*aa*cc)**(1/2) ) / (2*aa)
		rootB =(-bb - (bb*bb-4*aa*cc)**(1/2) ) / (2*aa)
	
		#rounds the roots to 2 places
		RrootA = round(rootA,2)
		RrootB = round(rootB,2)	
		
		#adds final roots to the rootArray	
		rootArray.append(RrootA)
		rootArray.append(RrootB)


		return rootArray

# prints the raw array	
print(discrimFunc(inputArray))

print(str(rootArray[0]) + " " + str(rootArray[1]))
