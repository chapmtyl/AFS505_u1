types_of_people = 10 # gives value to this variable
x = f"There are {types_of_people} types of people." # defines x

binary = "binary" # defines the variable binary
do_not = "don't" # defines the varaible do_not
y = f"Those who know {binary} and those who {do_not}." # defines y

print(x) #prints the x variable
print(y) #prints the y variable

print(f"I said: {x}") # prints i said: and x variable
print(f"I also said: '{y}'") # prints I also said: and y variable

hilarious = False #defines hilarious
joke_evaluation = "Isn't that joke so funny?! {}" # defines joke_evaluation

print(joke_evaluation.format(hilarious)) # prints joke_evaluation and hilarious.

w = "This is the left side of..." #defines w
e = "a string with a right side." # defines e

print(w + e) #prints w and e
