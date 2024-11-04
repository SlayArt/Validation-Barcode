
# verify the lenght of the number of the barcode, if its not 13 the bar code is invalid
def verif_lenght(bc):
    """
        a function to verify if the given barcode have the good lenght
        
        Args:
            bc : the number of the barcode
            
        Returns:
            return True if the barcode is the good lenght, False if it isn't 
    """
    
    return len(str(bc)) == 13 # return True if bc == 13 and False if it's not

# verify is there is only numbers in the barcode, if not the barcode is invalid
def only_numbers(bc):
    """
        a function to verify if the barcode is only composed of numbers
        
        Args:
            bc : the barcode
        
        Returns:
            return True if the number givent by the user is only composed of numbers, False if it isn't 
    """
    
    numbers = "1234567890" ; return all(char in numbers for char in str(bc)) #initialize all the numbers in variable numbers and verify if there is only numbers
"""
# without native function

def only_numbers(bc):
    numbers = "1234567890" # initialize all numbers in variable numbers
    for i in range(len(bc)): # crate a loop to check all character
        if bc[i] not in numbers: # if actual checking char is not in variable numbers
            return False # return False
        return True # if all char are in numbers return True
"""

# sum of all numbers with impairs position in the barcode
def add_impairs(bc):
    """
        a function to add all numbers with impairs position in the barcode
        
        Args:
            bc : the barcode
        
        Returns:
            returns the result of the addition of all numbers with impairs position
    """
    
    res = 0 ; return sum(int(str(bc)[i]) for i in range(0, len(str(bc))-1, 2)) # initialize a result as 0, create the sum of all numbers with impairs positions with a loop
# be careful, the loop start at 0 and not 1 because as humain 0 is pairs but a char[0] is the first char so a char with impairs index
"""
# without native function

def add_impairs(bc):
    res = 0 # initialize a result as 0 
    for i in range(0, len(bc)-1, 2): # create a loop to check all char with impairs position
        res += bc[i] # add to result all numbers with impairs position 
    return res # return final result
"""

#same as add_impairs() but with pairs positions
def add_pairs(bc):
        """
        a function to add all numbers with pairs position in the barcode
        
        Args:
            bc : the barcode
        
        Returns:
            returns the result of the addition of all numbers with pairs position
    """
    
    res = 0 ; return sum(int(str(bc)[i]) for i in range(1, len(str(bc))-1, 2))
# be careful, the loop start at 1 and not 0 because as humain 1 is impairs but a char[1] is the second char so a char with pairs index
"""
def add_impairs(bc):
    res = 0
    for i in range(1, len(bc)-1, 2):
        res += bc[i]
    return res
"""

# multiply a number by 3
def factor_three(bc):
    """
        a function to muliply by 3 the result of the function above add_pairs(bc)
        
        Args:
            bc : the barcode
            
        Returns:
            return the result of the multiplication of 3 and the result of add_pairs(bc)
    """
    
    return add_pairs(bc) * 3 # return the result of add_impairs() factor 3

# verify traitement
def traitement(bc):
    """
        a fucntion to add the result of add_impairs() and factor_three(), and substract the rest of the division by 10 (of the previous result) of 10
        
        Args:
            bc : the barcode
            
        Returns:
            return the result of this calcul
    """
    
    return 10 - ((add_impairs(bc) + factor_three(bc)) % 10) # make the sum of the result of add_impairs() and factor_three(), take the rest of the division by 10, substract the rest to 10

# main function, verify if the barcode is valid (barcode is given by user)
def validation_barcode(bc):
    """
        the main function, composed of all the previous function to verify if the barcode is valid or not
        
        Args:
            bc : the barcode
        
        Returns:
            Return True if the barcode is valid, False if it isn't
    """
    
    if only_numbers(bc): # if the barcode contains only numbers continue
        if verif_lenght(bc): # if the barcode is the correct lenght continue
            result_calcul = traitement(bc) # initialize result_calcul as the result of the function traitement()
            if result_calcul == int(str(bc)[-1]): # if result_calcul == last char of the barcode continue
                return True # if all conditions are True, return True, the barcode is valid
    return False # if one of this conditions is False, return False, the barcode is invalid

print(validation_barcode(4006381333936)) # call the main function to check if the barcode is valid
# example of valid barcode ----- 9782091726649
# example of invalid barcode ----- 4006381333936
