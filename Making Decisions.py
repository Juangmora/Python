'''
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward
and user-friendly.
'''

age = int(input("What is your age?  ")) # Enter your age here

if age > 21: # Is older then age specified reply
    print("You are old enough to drive.")
    print("You can also vote!")
    print("You can purchase alcohol.")
if age > 60: # Older then sixty, reply
    print("You are eligible for a senior discount sir.")
elif age <= 15: # Is younger then fifteen reply
    print("You cannot drive yet.")
    print("You are not old enough to vote.")
    print("You are too young to buy alcohol!")
    print("You can not get a senior discount.")
else:
    print("You can not get a senior discount.")
