#allowing each persons name to be passed in
def greeting(name):
  print('Hello', name)

greeting('Sharlene')
greeting('Rachelle')
greeting('Luana')

#creating function with multiple parameters
def about_me(fave_food, fave_animal, fave_place):
  print('I love to eat', fave_food, 'while petting my', fave_animal, 'on', fave_place)

about_me('loco mocos', 'hubbys dog', 'the bed')

#calling the functions with aruguments out of order
about_me("the beach", "sushi", "cat")

#allows to specify the names of the params as we want it to
about_me(fave_place="the beach", fave_food="sushi", fave_animal="cat")

def accept_phone(number, phone_type):
  print('The phone number', number, 'is a', phone_type, 'phone')

#passing the arguments as normal
accept_phone('555-1234', 'home')
accept_phone('555-5678', 'cell')
accept_phone('555-8765', 'work')

#global varaible
def greeting():
  print('Hello', name)

name = 'Boto'
greeting()

#global variable & local variable
def greeting():
    name = 'Sharlene'
    print('Whatup', name)
    #using both variables
    name = 'Luana'
    print('Hello', name)

    name = 'Rach'
    greeting()

#prints out only rach name
print(name)

#both variables used
