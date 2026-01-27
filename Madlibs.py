"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# Get info from user
player_name = input("What name would you like to use? ")
race = input("Choose a mythical race? ") # Examples: Elves, Dwarfs, Dragonborn
specialty = input("What is your specialty? ") # Examples: Summoner, warrior, mage, dragoon
weapon = input("What is your weapon of choice? ")
element = input("Choose an element that you resonate with. ") # Example: fire, water, wind, earth, lighting, dark, light

# My story
madlibs = (f"Welcome {player_name} to land of Spira! \nA place where the {race} live in chaos and war.\nAt birth the {race} are born with an affinity to the {element} element. \nThe {race} are specialist in the {specialty} class and are also masters with the {weapon}.\n With their specialty and weapon of choice at hand, now begins your journey for greatness!")

print(madlibs)
