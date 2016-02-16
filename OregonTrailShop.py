#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Gaddis, T. "Starting Out With Python 2nd ed"[PDF document] (Pearson, 2012) (Fall 2015).

#Title and introduction
print("                  ⋆ ✢ ✣ ✤ ✥ ✦ ✧ ✩    ")
print("~~~~~~~~~~~~~~~~~~ THE OREGON TRAIL ~~~~~~~~~~~~~~~~~~~")
print("                  ⋆ ✢ ✣ ✤ ✥ ✦ ✧ ✩    ")
print()
print("Welcome to Matt's General Store Independence, Missouri!")
print("The only place in town to buy things!")
print("Here is a list of what's for sale:")
print()
print("Oxen - 2 per yoke, $40.00 a yoke")
print("Food - $0.20 per pound")
print("Clothing - $10.00 a set")
print("Bullets - $2.00 a box")
print("Spare Parts - $10.00 each")
print()
#ask how many yokes user wants and calculate cost of yokes
yoke=(float(input("How many yoke would you like? "))*40) 
#format value to two decimal places
yokeF=format(yoke,'.2f') 
#print subtotal
print("Current Bill: $",yokeF)

#repeat for each item available for purchase 

food=(float(input("How many pounds of food would you like? "))*0.20)
foodF=format(food,'.2f')
sub=format(yoke+food,'.2f')
print("Current Bill: $",sub)
clothes=(float(input("How many sets of clothes would you like? "))*10.00)
clothesF=format(clothes,'.2f')
sub=format(yoke+food+clothes,'.2f') 
print("Current Bill: $",sub)#
bullets=(float(input("How many boxes of bullets do you want? "))*2.00)
bulletsF=format(bullets,'.2f')
sub=format(yoke+food+clothes+bullets, '.2f')
print("Current Bill: $",sub)
spare=(float(input("How many spare parts do you want? "))*10.00)
spareF=format(spare,'.2f')
sub=format(yoke+food+clothes+bullets+spare, '.2f')
print("Current Bill: $",sub)

total=sub #total bill is equal to most recent subtotal
print()

#display final receipt
print("   ~~~~~~~~~~")
print("    RECEIPT")
print("   ~~~~~~~~~~")
print("Oxen          $",yokeF)#
print("Food          $",foodF)
print("Clothes       $",clothesF)
print("Bullets       $",bulletsF)
print("Spare Parts   $",spareF)
print("_______________________")
print("Total:        $",total)


