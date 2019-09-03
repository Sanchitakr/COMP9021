# Written by *** for COMP9021
import re
from collections import OrderedDict, Counter



def reverse_letters(tuples): 
    new_tup = () 
    for k in reversed(tuples): 
        new_tup = new_tup + (k,) 
    return new_tup 
  
def convert_letters_to_number_dict(inputs=None):
    letters = []
    if inputs and len(set(inputs)) != len(inputs):
        return None
    if inputs is None:
        inputs = "MDCLXVI"
    inputs = inputs[::-1]
    for index in range(0, len(inputs), 2):
        letters.append((inputs[index], int(10 ** (index / 2))))
        if index + 1 < len(inputs):
            alph=inputs[index:index + 2]
            diff=(int(5*10 ** (index / 2)) - int(10 ** (index / 2)))
            letters.append((alph, diff))
            letters.append((inputs[index + 1], int(5*10 ** (index / 2))))
        if index + 2 < len(inputs):
            alph2=inputs[index] + inputs[index + 2]
            diff2=int(10 ** ((index + 2) / 2)) - int(10 ** (index / 2))
            letters.append((alph2,diff2 ))
        
        
#OrderedDict remembers the order that keys were first inserted
    return (OrderedDict(reverse_letters(letters)))


def roman_to_arabic(inputs, dicts=None):
    result = 0
    if dicts is None:
        dicts = convert_letters_to_number_dict()
    for i in range(len(inputs)):
        
        if inputs[i] not in dicts.keys():
            return None
        if inputs[i] == "_":
            return 0
        else:
            num = int(dicts[inputs[i]])
            if  len(inputs)>(i + 1)  and num<dicts[inputs[i + 1]]:
                result =result- num
            else:
                result =result+ num
    
    if inputs!=arabic_to_roman(result, dicts):
        return None
    else:
        return result


def arabic_to_roman(initial_arabic, dicts):
    result = []
    for roman, num in dicts.items():
#   num = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
#   romam = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    
    
        while initial_arabic >= num:
            result.append(roman)
            initial_arabic = initial_arabic- num
            
    return ''.join(result)

##In case the user inputs Please convert ***, then *** should be either a strictly
##positive integer (whose representation should not start with 0) that can be converted to a Roman number (hence
##be at most equal to 3999), or a valid Roman number; otherwise, the program should print out "Hey, ask me something that's not impossible to do!"

def first(inputs):
    param = inputs[2]
    if not re.match(r'^([1-9]|[1-3][0-9]{1,3})$', param):
        result = roman_to_arabic(param)
        
    else:
        dicts = convert_letters_to_number_dict()
        result = arabic_to_roman(int(param), dicts)

    if not result:
        print(f"Hey, ask me something that's not impossible to do!")
        
    else:
        print(f"Sure! It is {result}")

#In case the user inputs Please convert *** using ***, then the first ***
#should be a strictly positive integer (whose representation should not start with 0) 
#or a sequence of (lowercase
#or uppercase) letters and the second *** should be a 
#sequence of distinct (lowercase or uppercase) letters.

def second(inputs):
    if inputs[3] != "using":
        print("I don't get what you want, sorry mate!")
    else:
        roman_dicts = convert_letters_to_number_dict(inputs[4])
        if roman_dicts:
            if not re.match(r'^([1-9]|[1-9][0-9]+)$', inputs[2]):
                result = roman_to_arabic(inputs[2], roman_dicts)
                
            else:
                result = arabic_to_roman(int(inputs[2]), roman_dicts)
            if not result:
                print("Hey, ask me something that's not impossible to do!")
                
            else:
                print(f"Sure! It is {result}")
                
        if not roman_dicts:
            print("Hey, ask me something that's not impossible to do!")


#In case the user inputs Please convert *** minimally, then *** should be a
#sequence of (lowercase or uppercase) letters. The program will try and view *** as a generalised Roman number
#with respect to some sequence of generalised Roman symbols. If that is not possible, then the program should
#print out Hey, ask me something that's not impossible to do!
def third(inputs):
    if inputs[3] != "minimally":
        print("I don't get what you want, sorry mate!")
    elif re.match(r'\d', inputs[2]):
        print("Hey, ask me something that's not impossible to do!")
        


def please_convert():
    inputs = input('How can I help you? ').split(" ")
    if inputs[0] == "Please" and inputs[1] == "convert" and 3 <= len(inputs) <= 5 :
        if len(inputs) == 4:
            third(inputs)
        elif len(inputs) == 3:
            first(inputs)
        else:
            second(inputs)    
    else:
        print("I don't get what you want, sorry mate!")
please_convert()





