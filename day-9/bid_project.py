from art import logo

print(logo)

print("Welcome to the secret auction program.\n")
bid_dictionary = {}
is_Continue = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"matthew":222, "daniel":333 }
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not is_Continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dictionary[name] = bid

    other_Bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_Bidder == 'no':
        is_Continue = True
        find_highest_bidder(bid_dictionary)


print(bid_dictionary)

# max_value = max(bid_dictionary.values())
# print(max_value)
