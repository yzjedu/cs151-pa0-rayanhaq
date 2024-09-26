import cmath
#Cmath is imported because it is helps with the negative in the square root.
#Quadratic equation is ax**2+bx+c
#Quadratic formula is x = -b+ or - sqrt of b^2-4 * a * c / 2a

a = int(input("Input a:"))
# Variable for a value
b = int(input("Input b:"))
# Variable for b value
c = int(input("Input c:"))
# Variable for c value
# Important to store these in variables because one if we did not have them the code would not execute
# As well as it makes it more organizable.

#Calculating the discriminant
d = b**2 - 4 * a * c

#Calculate the formula
solution_1 =(-b + cmath.sqrt(d))/(2*a)
solution_2 =(-b - cmath.sqrt(d))/(2*a)

#Print the Solution
print("The solution to the quadratic equation is")
print(solution_1)
print(solution_2)


