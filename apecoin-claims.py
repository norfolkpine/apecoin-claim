# Find Unclaimed Apecoin

from web3 import Web3
import requests
import json

print("Apecoin Claim status")
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/29ac39e3896b46e6a181b62756193ded'))

# Get information about the latest block
w3.eth.getBlock('latest')

# Get the ETH balance of an address 
#balance = w3.eth.getBalance('0x1Ab584155F34e3876424FAA5044f3362Afbd6644')
#print(balance)

#ALPHA BAYC
#0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d
#alphaClaimed
#https://api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}/listings
#https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/9227/listings


#BETA MAYC
#0x60e4d786628fea6478f785a6d7e704777c86a7c6
#betaClaimed

#GAMMA BAKC
# 0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623
#gammaClaimed

apecoinABI = '[{"inputs":[{"internalType":"address","name":"_grapesTokenAddress","type":"address"},{"internalType":"address","name":"_alphaContractAddress","type":"address"},{"internalType":"address","name":"_betaContractAddress","type":"address"},{"internalType":"address","name":"_gammaContractAddress","type":"address"},{"internalType":"uint256","name":"_ALPHA_DISTRIBUTION_AMOUNT","type":"uint256"},{"internalType":"uint256","name":"_BETA_DISTRIBUTION_AMOUNT","type":"uint256"},{"internalType":"uint256","name":"_GAMMA_DISTRIBUTION_AMOUNT","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"AirDrop","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"AlphaClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"BetaClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_claimDuration","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_claimStartTime","type":"uint256"}],"name":"ClaimStart","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"GammaClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"ALPHA_DISTRIBUTION_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"BETA_DISTRIBUTION_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GAMMA_DISTRIBUTION_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"alpha","outputs":[{"internalType":"contract ERC721Enumerable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"alphaClaimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"beta","outputs":[{"internalType":"contract ERC721Enumerable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"betaClaimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimUnclaimedTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"gamma","outputs":[{"internalType":"contract ERC721Enumerable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"gammaClaimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"}],"name":"getClaimableTokenAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"grapesToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pauseClaimablePeriod","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_claimDuration","type":"uint256"}],"name":"startClaimablePeriod","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalClaimed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'



# Configure w3, e.g., w3 = Web3(...)
address = '0x025C6da5BD0e6A5dd1350fda9e3B6a614B205a1F'

contract_instance = w3.eth.contract(address=address, abi=apecoinABI)

# LOOP

file = open('MAYC4.txt', 'r')
Lines = file.readlines()

#Lines = [int(i) for i in Lines]


for line in Lines:
    row = line
    #print(row)

# read state:
    value = int(row)
    #bayc = str(contract_instance.functions.alphaClaimed(value).call())
    mayc = contract_instance.functions.betaClaimed(value).call()
    strMAYC = str(mayc)
    id = str(value)
    #print("BAYC " + "Token ID: " + id + ", Result: " + bayc)
    #print("MAYC " + "Token ID: " + id + ", Result: " + mayc)
    print("id: " + id)
    
    if mayc == False:
        #id = '9130'
        print("MAYC: " + id + ", " + strMAYC)
        url = ('https://api.opensea.io/api/v1/asset/0x60e4d786628fea6478f785a6d7e704777c86a7c6/' + id + '/listings?format=json')
        print(url)
        headers = {"Accept": "application/json", "x-api-key":"630620bae3cd45f09fb46a642d30934f"}
        response = requests.get(url, headers=headers)
        response = response.json()
        data = json.dumps(response)


        if not 'listings' in response or len(response['listings']) == 0:
            print("No Listing")
            with open('MAYC2-TEST.txt', 'a') as f:
                f.write(f'\n{id}')
                f.write(', ' + 'No Listing')
                f.write(', '+ url)
        else:
            current_price = (response['listings'][0]['current_price'])
            current_price = float(current_price) / 1000000000000000000
            price = str(current_price)
            print(price)

            with open('MAYC2-TEST.txt', 'a') as f:
                f.write(f'\n{id}')
                f.write(', '+ price + " ETH")
                f.write(', '+ url)