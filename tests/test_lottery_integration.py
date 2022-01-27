from brownie import Lottery, accounts, config, network
from scripts.deploy_lottery import deploy_lottery
from scripts.helper_functions import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, fund_with_link
from web3 import Web3
import pytest
import time

def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({'from': account})
    lottery.enter({'from': account, 'value': lottery.getEntranceFee()})
    lottery.enter({'from': account, 'value': lottery.getEntranceFee()})

    fund_with_link(lottery)
    lottery.endLottery({'from': account})
    time.sleep(100)

    assert lottery.recentWinner() == account
    assert lottery.balance() == 0