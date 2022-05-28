print("welcome to kombat zone roller coaster ride")
height = int(input(" what is your height \n"))
bill = 0
if height >=120:
  print("you can ride on the roller coaster")
  age = int(input("what is your age?"))
  if age <12:
    bill = 5
    print("children ticket is $5")
  elif age <=18:
    bill = 7
    print("teenage ticket is $7")
  elif age >=45 and age <= 55:
    print(" everything is okay, you can have a free ride")
  else:
    bill = 12
    print(" adult tickets is $12")
  want_photo = input(" do you want a photo taken ? Y or N\n")
  if want_photo == "Y":
    bill = bill + 3
    print(f"your final bill is $ {bill}")

else:
    print("you are not qualified , try again when you are taller")
