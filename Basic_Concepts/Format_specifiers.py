#format specifiers and format strings

#integer format specifiers

a=10
print("%d"%a)   #prints Decimal integer
print("%i"%a)   #signed integer same as decimal integer

#checks the digit length is five if not add the 5-digit length trailing spaces
print("%5d"%a)  

#pads with 0's to ensure 5 digits 
#or to fill the width to 5 digits
print("%.5d"%a)
print("%05d"%a)


print("%+d"%a)      #adds  + sign to positive numbers
print("%+5d"%a)     #adds + sign and chack for 5 length width space
#adds + sign and checks for 5 length width space if not 
#remaining spaces filled with 0 till 5 length including +
print("%+05d"%a)
#adds + sign and checks for 5 length width space if not 
#remaining spaces filled with 0 till 5 length Excluding +
print("%+.5d"%a)

print("%+d"%-10)    #it doesn't add + sign coz of negative numbers
print("%+d"%--10)   #it will add + sign coz -- will become positive
print("%+d"%---10)  #same as single -
print("%+d"%----10) #same as double -


#floating point format specifiers

#if we are directly printing the variable it will print single zero in decimal value
a=10
print(float(a))

a=float(input())
print(a)

#if we are using format specifier for float
#then we can get 6 decimal places
a=10
print("%f"%a)

a=23.56
print("%f"%a)

#checks the digit length is 3 if not add the 3-digit length trailing spaces
print("%3f"%a)
#checks the digit length is 13 if not add the 13-digit length trailing spaces
print("%13f"%a)

#print the float value with 2 decimal places
print("%.2f"%a)
#print the float value with 5 decimal places
print("%.5f"%a)
#print the float value with 10 decimal places
print("%.10f"%a)

#checks the digit length is 12 if not add the 12-digit length trailing spaces
#print the float value with 2 decimal places
print("%12.2f"%a)

#Secientific notation
#adds e notation for the float value
print("%e"%a)
#Secientific notation
print("%E"%a)

#%g or %G ->generat format -> works for real numbers
print("%g"%a)   #if you given float value it will print float value
print("%G"%10)  #if you given integer value it will print integer



#charecter format specifiers

#Prints the ASCII character for 65 ('A')
print("%c"%65)
#Prints the character itself ('A')
print("%c"%'A')
##checks the charecter or string length is five
#if not add the 5-charecter length trailing spaces
print("%5c"%'A')
#works as same as above example 4 spaces and charecter total 5
print("%5.c"%'A')
#. doesn't works for charecters
print("%.5c"%'A')


#string format specifiers

print("Hello")
print("Hello"[0])   #returns the first charecter
print("Hello"[-1])  #returns the last charecter 


#it will print the string to console
print("%s"%"Hello")

#minimum field width is 2 charecters
print("%2s"%"Hello")

#minimum field width is 10 charecters so that it leaves number - length of string spaces
print("%10s"%"Hello")

#limits the string to a maximum of 2 charecters
print("%.2s"%"Hello")

#limits the string to a maximum of 7 charecters
print("%.7s"%"Hello")

# Field width 10, but limits to 3 characters, so 7 leading spaces
print("%10.3s" % "Python")



#extras
print("%d"%10.45)  #prints integer value
#print("%d"%'4')     #TypeError
print("%c"%'5')     #prints charecter 5
print("%f"%23)  #prints float with 6 deciaml places
print("%s"%567) #prints 567 to console
print("\"%s\""%567) #prints 567 in double quotes
print("%s"%432.67)
print("\'%s\'"%432.67)
