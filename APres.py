# Functions for the formulae
# Finding nth term value
# a = first value
# b = second value_value is the value of the n term
# nth_term is the t
# # d = difference
# # nterm of the n_value

def nth_value():
    '''
    This function help to find the nth value when 1st and 2nd term are given..
    '''
    try :
        a = float(input("Enter the 1st term :"))
        b = float(input("Enter th 2nd term :"))
        n = float(input("Enter the nth term :"))
    except Exception as e:
        print("Please enter the appropriate values..", e)
        return nth_value()
    d = b - a
    nth = a + (n - 1)*d
    print (f"The value of {n}th term is {nth} ")
    # yes_no = str(input("Do you want the AP of the above values..? (y/n)"))
    # for i in yes_no:
    #     if yes_no == 'y':
    #         j = 0
    #         while True:
    #
    #             vals =
    #     elif yes_no == 'n':
    #         pass
    #     else:
    #         print("Enter appropriate alphabet :")
    # return yes_no
def nth_term():
    '''
    This function help to find the nth term while nth value, 1st and 2nd term are given..
    '''
    try:
        a = float(input("Enter the 1st term :"))
        b = float(input("Enter the 2nd value :"))
        nth_val= float(input("Enter the value of the term :"))
    except Exception as e :
        print("Please enter the appropriate values.." , e)
        return nth_term()
    d = b - a
    n_term = (nth_val - a + d)/d
    print (f"The term of {nth_val}th value is {n_term} ")

def Sum_n():
    '''
    This function helps in finding the sum of first n terms..
    '''
    try:
        a = float(input("Enter the 1st term :"))
        b = float(input("Enter the 2st term :"))
        n = float(input("Enter the number of nth terms :"))
    except Exception as e :
        print("Please enter the appropriate values :" , e)
        return rerun()                          # rerun for now..
    d = b - a
    Sum_n = n/2*(2*a + (n - 1)*d)
    print(f"\nThe sum of first {n} terms is {Sum_n}")

def Sum_all():
    '''
    This function helps to find the last term of the AP..
    '''
    try:
        a = float(input("Enter the 1st term :"))
        l = float(input("Enter the last term :"))
        n = float(input("Enter the nth term :"))
    except Exception as e:
        print("Please enter the appropriate values :" , e)
        return Sum_all()
    sum_all = (a + l)*n/2
    print(f"\n The sum of all terms is {sum_all}")

# Running in loop
def run():
    '''
    This function helps to run the whole code at once..
    '''
    print("________For finding nth_value press 1______\n"
          "________For finding nth_term press 2_______\n"
          "________For finding sum of first n terms press 3______\n"
          "________For finding Sum of all terms press 4_________")
    # Input statement for using required formulae
    num = int(input("Enter what sort for calculation you what :"))
    while True:
        if num == 1:
            nth_value()
            print("\nThank You for using my program..")
        elif num == 2:
            nth_term()
            print("\nThank You for using my program..")
        elif num == 3:
            Sum_n()
            print("\nThank You for using my program..")
        elif num == 4:
            Sum_all()
            print("\nThank You for using my program..")
        else:
            print("Please enter appropriate number..!!")
        break
    # Reruning the program..
    while True:
        rerun()

# Rerun the program..
def rerun():
    '''
    This function help to rerun the whole program..
    '''
    y_n = str(input("\nWould you like to rerun the program..? (y/n)"))
    if y_n == "y" :
        print("...Ok rerunning the program...\n")
        run()
    elif y_n == "n":
        print("\nOnce again..thanks for using my program..")
        quit()
    else:
        print("\nPlease enter appropriate alphabet..!!")
        return rerun()

