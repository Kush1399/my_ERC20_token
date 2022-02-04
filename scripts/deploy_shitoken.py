from brownie import ShiToken
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000, "ether")

def deploy_shi_token():
    account = get_account()
    shi_token = ShiToken.deploy(INITIAL_SUPPLY, {"from": account})

def main():
    deploy_shi_token()
