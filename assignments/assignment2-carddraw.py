import requests

#get request
url = "https://deckofcardsapi.com/api/deck/vn1akv2xj2wc/draw/?count=5"
response = requests.get(url)
data = response.json()

#getting the data of the cards and the remaining cards
cards_list = data["cards"]
cards_remaining = data["remaining"]
print("Your drawn cards are:\n")

#printing the value and suit of the cards drawn
for cards in cards_list:
    print("{} of {}".format(cards["value"], cards["suit"]))

#showing how many cards are left in the deck
print("\nThere are {} cards remaining in the deck.".format(cards_remaining))

