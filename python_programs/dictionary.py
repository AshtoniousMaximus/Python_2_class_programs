# dictionary
# created by Ashton Pankey
# Revised on 11/02/2024

# creates an average_grade function that takes a dictionary and returns the average grade
def average_grade(n):
    # creates a list of values from the dictionary
    grades = list(n.values())
    # creates the average from the sum of the grades over the amount of grades
    average = sum(grades)/len(grades)
    # returns a print of the average grade of the student
    return print(f"average grade: {average}\n")

# creates a few dictionaries for each person's grades
bill = {"History": 85, "Math": 90, "Art": 81, "Science": 95}
ted = {"History": 83, "Math": 85, "Art": 95, "Science": 76}
lisa = {"History": 95, "Math": 99, "Art": 91, "Science": 110}
bart = {"History": 64, "Math": 73, "Art": 72, "Science": 61}
marge = {"History": 90, "Math": 86, "Art": 94, "Science": 87}
homer = {"History": 2, "Math":5, "Art": 26, "Television": 85, "Beer drinking": 94, "Doughnut eating": 99}

# creates a dictionary called grade_book that contains keys that are assigned to each person's grades
grade_book = {"Bill": bill, "Ted": ted, "Lisa": lisa, "Bart": bart, "Marge": marge, "Homer": homer}

# prints the grade_book dictionary
print(grade_book)

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)

# removes homer's "class" Beer drinking from the dictionary
homer.pop("Beer drinking")

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)

# removes homer's "class" Television from the dictionary
homer.pop("Television")

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)

# removes homer's "class" Doughnut eating from the dictionary
homer.pop("Doughnut eating")

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)

# adds the class Science to Homer's grades 
homer["Science"] = 12

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)

# updates homer's History grade to 13
homer.update({"History": 13})

# creates a for loop that runs through the items in the dictionary grade_book
for key, value in grade_book.items():
    # prints the person's grades are and prints the dictionary at value
    print(f"{key}'s grades are: \n {value}")
    # computes the average of that person's grade and spits it out from the function's return 
    average_grade(value)
