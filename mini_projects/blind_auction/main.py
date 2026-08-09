import art

print(art.logo)

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the the bid of {highest_bidder}")

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        find_highest_bidder(bids)