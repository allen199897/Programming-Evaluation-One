print(""" 
$$$$$$\                        $$\     $$\           
$$  __$$\                       $$ |    \__|          
$$ /  $$ |$$\   $$\  $$$$$$$\ $$$$$$\   $$\ $$$$$$$\  
$$$$$$$$ |$$ |  $$ |$$  _____|\_$$  _|  $$ |$$  __$$\ 
$$  __$$ |$$ |  $$ |\$$$$$$\    $$ |    $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ | \____$$\   $$ |$$\ $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |$$$$$$$  |  \$$$$  |$$ |$$ |  $$ |
\__|  \__| \______/ \_______/    \____/ \__|\__|  \__|
""")

#_______________QUESTION 2 : TRIANGLE_______________

import math
print("This program will calculate the area of a triangle")
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
s = a+b+c/2
area = round(math.sqrt((s*(s-a)*(s-b)*(s-c))), 2)


print ('\n' "therfor the area of the triangle is: ", area)

#_______________QUESTION 3 : BUDGET_______________
import random
import math
print('\n' "this is a budget plan")
b = int(input("Please enter your mounthly budget"))
f = (random.randint(50,100))
c = (random.randint(50,100))
e = (random.randint(50,100))
r = (random.randint(700,1500))
print('\n '"here is your spending on food", f)
print("here is your spending on clothing", c)
print( "here is your spending on entertainment", e)
print("here is your spending on rent", r)
total_s = f+c+e+r

print('\n '"your total spending is", total_s)
total = b - total_s

print("your total leftover is", total)

p1 = round((b/r), 2)
p2 = round((b/c), 2)
p3 = round((b/e), 2)
p4 = round((b/f), 2)
print('\n' "therefor your precentage of rent is", p1)
print("therefpr your precentage of clothing is", p2)
print("therefor your precentage of entertainment is", p3)
print("therefor your precentage of food is", p4)

