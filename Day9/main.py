import art

print(art.logo)

auction = []

#start the auction program
print("Welcome to the secret auction program.")
name = input('What is your name?: ')
bid = input("What's your bid?: $ ")
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n") 

#add a new bid to the auction list
def add_new_bid(name,bid):
    auction.append({
        "name": name,
        "bid":bid
    })

#if other bidders are entered, the program will ask for a new bid.Otherwise, the program will 
#find the max bid value and print out the winner of this auction .

while other_bidders.lower() == 'yes':
    add_new_bid(name,bid)
    print(auction)

    name = input('What is your name?: ')
    bid = input("What's your bid?: $ ")
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n") 

# before ending the bid, add the last bidder info. to the list
add_new_bid(name,bid)

# the max() function is used to find the dictionary with the largest 'bid' value. 
# The 'key' parameter specifies a function that calculates the comparison value for 
# each dictionary. In this case, the 'lambda' function extracts and converts the 'bid' 
# value to an integer for comparison. The result of max() is the dictionary with the 
# largest 'bid' value, and we can then directly access its 'bid' value to print it out.

winner_value = max(auction, key = lambda x: int(x["bid"]))
print(f"The winner is {winner_value['name']} with a bid of {winner_value['bid']}.")




