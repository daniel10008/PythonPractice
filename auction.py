bid_dictionary = {}

def find_highest_bidder ():
    highest_bid =0
    highest_bid_name = ""
    for key,value in bid_dictionary.items():
        if int(value)>int(highest_bid):
            highest_bid =value
            highest_bid_name=key
    print(f"the highest bid is {highest_bid_name} and it costs, {highest_bid}")
def auction():
    option_keeps_getting_called = True
    print("Welcome to the Auction")
    while option_keeps_getting_called:
        name = input("What is the name of something you want to put into the Auction: ")
        bid = input(f"What is the price you would like your {name} to be: ")
        bid_dictionary.update({name:bid})
        any_other = input("Is there other users who want to bid?: ")
        if any_other.lower() =="yes":
            option_keeps_getting_called =True
        else:
            option_keeps_getting_called = False
            find_highest_bidder()
auction()

