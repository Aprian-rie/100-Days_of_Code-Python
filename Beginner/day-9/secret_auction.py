from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret Auction program")
bidders = {}
bids_list = []
any_bidders = True
while any_bidders:
  bidder_name = input("What's your name: ?")
  bidders[bidder_name] = int(input("What's your bid:? "))
  ask_bidder = input("Are there other bidders: yes or no: ").lower()
  clear()
  if ask_bidder == 'no':
    any_bidders = False
for name in bidders:
  bids_list.append(bidders[name])
highest_bid = max(bids_list)
highest_bidder = [i for i, k in bidders.items() if k == highest_bid][0]
print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
