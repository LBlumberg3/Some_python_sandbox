carpet_quote_estimator()


mySpecialPromoCode = 'ADAROCKS'
# Method one - prevent the installation cost from being added at all

# modified line 73 in Val's code:
if i == 'installation' and promocode != mySpecialPromoCode: # Scenario A - no promo code 
    options_value += options_map['installation']
elif i == 'installation' and promocode == mySpecialPromoCode: # Scenario B - correct promo code
    options_list['installation']['price'] = 0




# Method two - allow the installation cost, then remove it later 

# unmodified line 73 in Val's code:
if i == 'installation':
    subtotal += options_map[i]

# Later in the code

if promo_code == 'ADAROCKS'
    subtotal -= options_map['installation']


# other examples
options_dictionary = { # all the options that ADA flooring is letting their customers choose 
    'installation': 123,
    'delivery': 234
}

carpet_type_dictionary = {
    ''
}
# options list - ways to handle
# option 1: use a list, iterate through it 
def check_options(options_list): # options_list is the group of options that the customer chose
    for i in options_list: # for each of the options the customer chose
        # Essentially, check each option against your "known" list of options
        if i not in options_dictionary:
            print("Not a recognized option: " + i) # if the option of "house cleaning" was included, this would catch it

    if(options[0] == 'installation' and promocode == 'ADAROCKS'):
        subtotal += 0 # Promo code is correct
    elif (options[0] == 'installation' and promocode != 'ADAROCKS'):
        subtotal += options_dictionary['installation']

    

result0 = carpet_cost_estimator([10, 10], "", ['installation'], "")


def check_carpet_type(carpet_type):
    if()




######################################3
# Separate example - list of dictionaries
#########################

friend_list = [
    {'name': 'Alice', 'birthYear': 2000, 'favMovie': 'Dune'},
    {'name': 'Bob', 'birthYear': 1990, 'favMovie': 'Cocaine Bear'}
    {'name': 'Eve', 'birthYear': 1980, 'favMovie': 'Terminator'}
]

best_friends_fav_movie = friend_list[0]['favMovie']
print (best_friends_fav_movie)