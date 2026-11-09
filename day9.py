
print("""
______
/ \
    )________(

| """""""" | _. -._,.---------., _. -._
| | | | | | |
| ________ | _. -._,.---------., _. -._ |
)________(
/ __________ \
      . - -----------.
/ ______________\

""")



def finding_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if  bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} and the highest bidder is {highest_bid}")


other_bidder = True
User_name_and_bid = {}

while other_bidder:
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid? "))
    availability_of_other_bidders = input("Are there any other bidders? type 'yes' or 'no' ")
    User_name_and_bid["name"] = bid_amount

    if availability_of_other_bidders == "yes":
         print("\n"*100)

    elif availability_of_other_bidders == "no":
        other_bidder = False
        finding_highest_bidder(bidding_dictionary=User_name_and_bid)











