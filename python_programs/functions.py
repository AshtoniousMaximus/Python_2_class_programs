# Functions
# created by Ashton Pankey
# revised on 09/12/2024



# FUNCTION 1 uses five inputs and returns a number
def steam_horsepower_calculator(pressure,stroke,acting,area,rpm):
    """
    this takes multiple inputs to determine the horsepower of a steam engine
    
    """
    # multiplies the functions together to determine the output power of the steam engine
    power = (float(pressure)*float(stroke)*int(acting)*float(area)*float(rpm))/33000
    return power



# FUNCTION 2 takes an input from the user and returns an encoded version
def encoder_function(uncoded):
    """
    takes the input from the user and encodes it
    
    """
    # creates a map for the translate function to reference when encoding the user input
    reverser = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA")
    # returns the message by translating the uncoded message into an encoded one using the translate function
    return uncoded.translate(reverser)
    

# FUNCTION 3 takes an input from the user and returns a list
def planet_age(year):
    """
    takes a user input age and tells how old they are in different planetary years
    """
    # creates a list called ages
    ages = []
    # multiplies the value year by the ratio of earth years to other years
    mercury_age = year*365/88
    venus_age = year*365/224.701
    earth_age = year
    mars_age = year*365/687
    jupiter_age = year*365/4333
    saturn_age = year*365/10759
    # adds the description and the amount of years into the list
    ages.append("Mercury years:")
    ages.append(mercury_age)
    ages.append("Venus years:")
    ages.append(venus_age)
    ages.append("Earth years:")
    ages.append(earth_age)
    ages.append("Martian years:")
    ages.append(mars_age)
    ages.append("Jupiter years:")
    ages.append(jupiter_age)
    ages.append("Saturn years:")
    ages.append(saturn_age)
    # returns the list ages
    return ages
    

# FUNCTION 4 takes a user input and returns a string
def planet_weight(pounds):
    """
    this takes a user input for weight and returns the weight of the user on most of our planets
    """
    # creates a list called weight
    weight = []
    # multiplies the value weight by the ratio of earth weight to planetary gravity compared to the earth
    mercury_weight = pounds*1*.38
    venus_weight = pounds*0.9
    earth_weight = pounds
    mars_weight = pounds*0.38
    jupiter_weight = pounds*2.53
    saturn_weight = pounds*1.07
    # adds the description and the amount of pounds into the list
    weight.append("Mercury weight:")
    weight.append(mercury_weight)
    weight.append("Venus weight:")
    weight.append(venus_weight)
    weight.append("Earth weight:")
    weight.append(earth_weight)
    weight.append("Martian weight:")
    weight.append(mars_weight)
    weight.append("Jupiter weight:")
    weight.append(jupiter_weight)
    weight.append("Saturn weight:")
    weight.append(saturn_weight)
    # returns the list weight
    return weight
    

# FUNCTION 5 takes a user input sentence and returns a vowel-less string
def vowel_remover(noVowel):
    """
    takes the user input sentence and replaces all of the vowels, capitalized or lowercase
    """
    # uses the .replace function to remove every vowel other than 'y' because i dont care about y
    vowel = noVowel.replace("a","")
    vowel = vowel.replace("A","")
    vowel = vowel.replace("e","")
    vowel = vowel.replace("E","")
    vowel = vowel.replace("i","")
    vowel = vowel.replace("I","")
    vowel = vowel.replace("o","")
    vowel = vowel.replace("O","")
    vowel = vowel.replace("u","")
    vowel = vowel.replace("U","")
    return(vowel)
        








print("functions menu")
while True:
    
    option = input("1:Steam power, 2:encoded message, 3:Planetary age calc, 4:Planetary weight calc, 5:Vowel remover\n")
    if (int(option) == 1):
        print("STEAM ENGINE HORSEPOWER CALCULATOR")
        # creates a set of inputs that collect the steam engine parameters
        pressure = input("what is the mean effective pressure of your boiler (in PSI)?\n")
        stroke = input("what is the stroke (in feet) of your engine?\n")
        acting = input("is your engine 1, single acting, or 2, double acting?\n")
        area = input("what is the area (in square inches) of your cylinder?\n")
        rpm = input("how many revolutions per minute does your engine achieve?\n")

        # prints the power of the steam engine
        print(f"your engine produces {steam_horsepower_calculator(pressure,stroke,acting,area,rpm)} horsepower")
        break
        
    elif(int(option) == 2):
        # prints the function selected
        print("message encrypter")
        # creates a user input called message
        message = input("what message would you like encoded?\n")
        # sends the input into the encoder function to reverse the letters
        coded = encoder_function(message)
        # prints the encoded message
        print(f"your encoded message is: {coded}")
        # sends the message back through the function to decode the message and prints the decoded message
        print(f"your decoded message is: {encoder_function(coded)}")
        # breaks the loop
        break
    elif(int(option) == 3):
        # takes the user input 
        age = int(input("how old are you in earth years?\n"))

        # sends the user input into the function planet_age
        print("here is a list of your age on other planets")
        # prints the list of different planetary ages
        print(planet_age(age))
        break
    elif(int(option) == 4):
        # takes the user input 
        weight = int(input("what is your weight in pounds?\n"))

        # sends the user input into the function planet_age
        print("here is a list of your weight on other planets")
        # prints the list of different planetary ages
        print(planet_weight(weight))
        break
    elif(int(option) == 5):
        # creates a user input for a sentence string
        sentence = str(input("type a sentence to have vowels removed\n"))
        # prints what the user typed
        print(sentence)
        # uses the vowel_remover function to remove every vowel
        print(vowel_remover(sentence))
        break
    else:
        print("invalid input, try again")

