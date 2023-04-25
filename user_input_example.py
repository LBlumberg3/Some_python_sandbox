def get_carpet_quote(room, userCarpetType, userQuoteOptions, userPromoCode): 
    print("I'm here!!!")

options_dictionary = {
    'installation': 100,
    'delivery': 123,
    'back_massage': 100000
}

roomLength = input("Enter in the room length: ")
roomWidth = input("Enter in the room width: ")
room = [roomLength, roomWidth]

userPromoCode = ""
userPromoCode = input("Please add a promo code, or nothing if you aren't cool: ")

userCarpetType = ""
userCarpetType = input("Please specify the type of carpet: ")

userQuoteOptions = []
inputOption = ""
while inputOption != 'continue':
    inputOption = input("Please add a valid option for your quote: ")
    if(inputOption == 'exit'):
        break # get out of the while loop
    if(inputOption not in options_dictionary):
        print("That is not a valid option!")
    userQuoteOptions.append(inputOption)

quote_cost = get_carpet_quote(room, userCarpetType, userQuoteOptions, userPromoCode)
print(quote_cost)