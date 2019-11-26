import snap_info as snap
import pesquisa_facebook as search
import find_interest_ids as find_ids
from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
import sys
import json

token = "EAAbPAyrnxo0BAPzWuLX7rwvEQjsJqgapZB72uA3zPLY7JYwUFklwHHZAg5QDvntzLNejvpORZCVHnjS0aLyLZBGTl8qtiVh3oPB6Nz4TAonq2KxCv14Jsci5sja54rhDWOHTACefiqzIGneW8wPYYgreJ738FVtHr3aMKZB963QZDZD"
act_id = "516894385544698"
secret = "-"

def get_ad_account():
    
    if secret != '-':
        FacebookAdsApi.init(access_token=token, app_secret=secret, api_version='v4.0')
    else:
        FacebookAdsApi.init(access_token=token, api_version='v4.0')
    account = AdAccount('act_' + act_id)
    return account

def main():
    dicionario_aux = {}
    with open('snap.json') as f:
        dicionario_aux = json.load(f)
    ids_vector = []
    for marca in dicionario_aux:
        print(marca['name'])
        ID = find_ids.remote(marca['name'])
        ids_vector.append(ID)
        print(ids_vector)
    account = get_ad_account()
    for id in ids_vector:
        search.get_politicians_distribution(account,id)



if __name__ == "__main__":   
    main()