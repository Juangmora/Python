'''
Write the program "99 Bottles of Beer on the Wall" using a while loop. 
Be mindful to change the word 'bottles' to 'bottle' when down to the last one.
 You must do the full 99 bottles; the sample shows the last 3 verses.
'''

bottles = 99 # Variable where the countdown begins

while bottles >= 2: # Stopping at 2 so countdown ends with 1 
    print(bottles , 'Bottles of beer on the wall')
    print(bottles , 'Bottles of beer')
    print('Take one down, pass it around')
    print(bottles -1 , 'Bottles of beer on the wall!')
    bottles -= 1 # Variable that subtracts by 1

else:
    bottles == 2 # Variable used for last part of the countdown
    print('1 Bottle of beer on the wall')
    print('1 Bottle of beer')
    print('Take one down, pass it around')
    print('No bottles of beer on the wall!')
   