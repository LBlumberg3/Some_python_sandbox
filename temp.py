friend_list = [
    {'name': 'Alice', 'birthYear': 2000, 'favMovie': 'Dune'},
    {'name': 'Bob', 'birthYear': 1990, 'favMovie': 'Cocaine Bear'},
    {'name': 'Eve', 'birthYear': 1980, 'favMovie': 'Terminator'}
]

def main():
    # 
    best_friends_fav_movie = friend_list[0]['favMovie']
    print (best_friends_fav_movie) # Should print 'Dune'

    # changing Alice's favorie movie to a superior one
    myFavoriteMovie = "Amsterdam"
    friend_list[0]['favMovie'] = myFavoriteMovie


##################

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
    if(inputOption not in options_dictionary) # assume that options_dictionary already exists
        print("That is not a valid option!")
    userQuoteOptions.append(inputOption)

quote_cost = get_carpet_quote(room, userCarpetType, userQuoteOptions, userPromoCode)
print(quote_cost)





userDimm = input("Enter in comma-delimited dimmensions for room: ")
dimmList = userDimm.split('|') # takes in a string, "splits" it every time it sees the pparameter 
# 10| 10|10|11|11
# [10, 10,10,11,11]