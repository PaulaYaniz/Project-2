# In this code there are 3 ways of doing the program. 
# The first is from 1 to 9 upwards and downwards.
# In the second the user can choose with what number to start.
# The last one converts decimal numbers 

# -*- coding: utf-8 -*-

# ___________________________________________________________________________

# FROM 1 TO 9 UPWARDS AND DOWNWARDS

direction = input("Do you want to go upwards or downwards? ")
direction = direction.lower()

if direction == "upwards":
  a = 0
  while a < 10:
    print(a)
    a += 1

elif direction == "downwards":
  a = 9
  while a > 0:
    print(a)
    a -= 1

else:
  print("Incorrect direction. Please write upwards or downwards.")

# ___________________________________________________________________________

# FROM A GIVEN NUMBER UPWARDS AND DOWNWARDS

direction = input("Do you want to go upwards or downwards? ")
direction = direction.lower()
n = int(input("Which number do you want to start with? "))

if direction != "upwards" and direction != "downwards":
  print("Incorrect direction. Please write upwards or downwards.")

if n < 1 or n > 10:
  print("Incorrect numbers. Please write a number between 1 and 9.")

elif direction == "upwards":
  while n < 10 and n > 0:
    print(n)
    n += 1

elif direction == "downwards":
  while n > 0 and n < 10:
    print(n)
    n -= 1

# ___________________________________________________________________________

# OTHER WAY TO DO IT
# FROM A GIVEN NUMBER UPWARDS AND DOWNWARDS

direction = input("Do you want to go upwards or downwards? ")
direction = direction.lower()
n = int(input("Which number do you want to start with? "))

if direction != "upwards" and direction != "downwards":
  print("Incorrect direction. Please write upwards or downwards.")

if n < 1 or n > 10:
  print("Incorrect numbers. Please write a number between 1 and 9.")

else:

  while n < 10 and n > 0:
    if direction == "upwards":
      print(n)
      n += 1

    elif direction == "downwards":
      print(n)
      n -= 1

input()

# ___________________________________________________________________________

"""# 1 to 9 upwards and downwards - Binary Morse system"""

direction = input("Do you want to go upwards or downwards? ")
direction = direction.lower()

n = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001"]
n[0] = "····"
n[1] = "···-"
n[2] = "··-·"
n[3] = "··--"
n[4] = "·-··"
n[5] = "·-·-"
n[6] = "·--·"
n[7] = "·---"
n[8] = "-···"
n[9] = "-··-"

if direction == "upwards":
  a = 1
  while a < 10:
    print(n[a])
    a += 1

elif direction == "downwards":
  a = 9
  while a > 0:
    print(n[a])
    a -= 1

else:
  print("Incorrect direction. Please write upwards or downwards.")
