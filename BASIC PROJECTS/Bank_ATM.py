import sys
import time

print("Welcome to Taiwo Forbes Banking ATM")
restart = ["YES","y","Y"]
dont_restart = ["n", "No","no","N"]
withdraw_amount = [10,20,50,100]
Pay_In_amount = [100,500,1000,2000]
attempt = 3
balance = 30000
while attempt >= 0:
    pin = int(input("Enter your 4 digit pin which is 1234 by default: "))
    if pin == (1234):
        print("You have entered the correct pin")
        while restart not in dont_restart:
            print("Enter 1 to check your Balance\n")
            print("Enter 2 to to make withdrawal\n")
            print("Enter 3 to Pay In\n")
            print("Enter 4 to Return Card\n")
            print()
            option = int(input("What would you like to choose: "))
            if option == 1:
                print("Please wait while we retrieve your Balance......\n")
                time.sleep(1)
                print("Your Balance is {}".format(balance))
                restart = input("Would you like to perform another Transaction:[y/n]\n")
                if restart in dont_restart:
                    print("Thank You")
                    sys.exit()
            elif option == 2:
                print("How much would you like to withdraw? \n10\t\t20\n50\t\t100\n")
                withdraw = float(input("Enter Amount\n"))
                if withdraw in withdraw_amount:
                    balance = balance - withdraw
                    print("Please wait while we process your request......\n")
                    time.sleep(1)
                    print("You Withdraw {}.\nYour new Balance is {}".format(withdraw,balance))
                    restart = input("Would you like to perform another Transaction:[y/n]\n")
                    if restart in dont_restart:
                        print("Thank You")
                        sys.exit()
                elif withdraw not in withdraw_amount:
                    print("Amount Unspecified, Please Re-try")
                    restart = "YES"
                elif withdraw == 1:
                    withdraw = float(input("Enter Desired Amount"))
            elif option == 3:
                print("How much would you like to Pay-In? \n100\t\t500\n1000\t\t2000\n")
                Pay_In = float(input("Enter Amount\n"))
                print("Please wait while we process your request......\n")
                time.sleep(1)
                if Pay_In in Pay_In_amount:
                    balance = balance + Pay_In
                    print("You Pay-In {}.\nYour new Balance is {}".format(Pay_In,balance))
                    restart = input("Would you like to perform another Transaction:[y/n]\n")
                    if restart in dont_restart:
                        print("Thank You")
                        sys.exit()
            elif option == 4:
                print("Please wait whilst your card is Returned....\n")
                time.sleep(2)
                print("Thank you for your service")
                sys.exit()
    elif pin != (1234):
        attempt = attempt - 1
        print("Incorrect Password,you've {} attempt left".format(attempt))
        if attempt == 0:
            print("You've exhaust you attempt")
            sys.exit()