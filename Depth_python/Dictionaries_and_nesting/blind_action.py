import os

clear = lambda: os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def starting():
    print(logo)
    print("Welcome to the secret auction program \n")
    name_input = input("What is your name?: \n")
    current_bid = input("What\'s your bid: $\n")
    bidders_check = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    bidders = []
    highest_bid =0
    bid_dic={
        "name":name_input,
        "bid":current_bid
    }
    bidders.append(bid_dic)
    checking_auction(bidders_check= bidders_check,bidders=bidders,highest_bid=highest_bid)
   
      
def checking_auction(bidders_check,bidders,highest_bid):
    while bidders_check == "yes":
        clear()
        name_input = input("What is your name?: \n")
        current_bid = input("What\'s your bid: $\n")
        bid_dic={
            "name":name_input,
            "bid":int(current_bid)
        }
        bidders.append(bid_dic)
        print(bidders)
        bidders_check = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    clear()
    for index in range(len(bidders)):
        if int(bidders[index]['bid']) > highest_bid and int(bidders[index]['bid']) > int(bidders[index - 1]['bid']):
            highest_bid = int(bidders[index]["bid"])
            print(f"The highest bid is from {bidders[index]['name']} with ${highest_bid}")

    


if __name__ =="__main__":
    starting()