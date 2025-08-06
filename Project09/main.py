def getHigherBid(bidDictionary):
    higherBid = 0
    for person in bidDictionary:
        bid = bidDictionary[person]
        if bid > higherBid:
            higherBid = bid
            #return higherBid
    print(f'{person} : Bid = {bid}' )

bidDictionary = {}
auction = True
while auction:
    name = str(input('Whats the name? '))
    bid = float(input('Whats the bid? '))
    bidDictionary[name] = bid
    continueAuction = str(input('Should continue the auction? "yes" or "no"'))
    if continueAuction == "no":
        getHigherBid(bidDictionary)
        auction = False