'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
'''


def getPerson (firstName, lastName, age ):
    return {
      "firstName": firstName,
      "lastName": lastName,
      "age": age
    }
    
    
    
print(getPerson('Marcelo', 'Mariath', 40))
