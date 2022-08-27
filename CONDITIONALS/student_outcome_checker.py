"""
    Write a program to find out  whether a student is pass or fail if it
    requires total of 40% and atleast 33% in each subject to pass.
    Requirement: Assume three subject and take mark as an input from the user
"""


sub1,sub2,sub3 = input("Enter your marks:").split()
sub1,sub2,sub3 = int(sub1), int(sub2), int(sub3)
total = (sub1 + sub2 + sub3) / 3 # Sum of all to 100 percentage
if total >= 40: # First condition to check is those marks is within the specified range
    if sub1 >= 33 and sub2 >= 33 and sub3 >= 33: # Nested condition if the first is true
        print("Congratulations you passed all subjects")
    else:
        print("Sorry, you failede because one of your subject isnt up to 33%")
else: # is the total marks is not up to the specified range, this should get executed
    print("Your total isnt up to 40%") 
