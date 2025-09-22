'''
Write a Python program to find and print all numbers divisible by 7 between 1 and 300.
 Use a for loop and the modulus operator (%).
'''

# These variables will define the starting and ending numbers of the range
start_num = 1
end_num = 300

print(f"Numbers divisible by 7 between {start_num} snd {end_num}:")

for num in range(start_num, end_num + 1):
    if num % 7 == 0: # This part of the code will check if the number is divisible by 7
        print(num)
