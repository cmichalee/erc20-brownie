from scripts.helpful_scripts import get_account
from brownie import TNAToken, config, network


def deploy_token():
    initial_supply = 1000000000000000000000
    account = get_account()
    print(f"Deploying TNAToken with initial supply of {initial_supply} tokens!")
    token = TNAToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed TNAToken Supply!")


def check_deployer_balance():
    account = get_account()
    deployer_balance = TNAToken[-1].balanceOf(account)
    print(f"Deployer Balance is {deployer_balance}")


def main():
    deploy_token()
    check_deployer_balance()
