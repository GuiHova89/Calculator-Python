a = None
b = None


def menu():
   a = float(input("Please type the first number: "))
   b = float(input("Please type the second number: "))
   choice = ""

   while choice != "A" and choice != "a" and choice != "M" and choice != "m" and choice != "S" and choice != "s" and choice != "D" and choice != "d":
      choice = input("Please select the math operation A (Addition), S (Subtraction), M (Multiplication) and D (Division) ")

      if choice == "A" or choice == "a":
        c=float("{:.2f}".format(a+b))
        print("the result is: ", c)
        restart()
      elif choice == "S" or choice == "s":
        c=float("{:.2f}".format(a-b))
        print("the result is: ", c)
        restart()
      elif choice == "M" or choice == "m":
        c=float("{:.2f}".format(a*b))
        print("the result is: ", c)
        restart()
      elif choice == "D" or choice == "d":
        c=float("{:.2f}".format(a/b))
        print("the result is: ", c)
        restart()
      else:
        print("You chose a different operation. Type A for Addition, S for Subtraction, M for Multiplication and D for Division.")


def restart():
   choice = ""

   while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
      choice = input("Would you like to continue and do another operation? Y for Yes and N for No ")

      if choice == "N" or choice == "n":
        print("Thank You!")
        exit()
      elif choice == "Y" or choice == "y":
        return menu()
      else:
        print("Please type Y to continue or N to close the calculator.")


menu()


# comment