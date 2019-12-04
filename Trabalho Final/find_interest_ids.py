# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.api import FacebookAdsApi
# import facebookads.adobjects.targeting.Targeting
from facebookads.exceptions import FacebookError
from unicodedata import normalize

import json, os, sys
import time, gzip

# https://developers.facebook.com/docs/marketing-api/targeting-search/
token = "EAAbPAyrnxo0BAPzWuLX7rwvEQjsJqgapZB72uA3zPLY7JYwUFklwHHZAg5QDvntzLNejvpORZCVHnjS0aLyLZBGTl8qtiVh3oPB6Nz4TAonq2KxCv14Jsci5sja54rhDWOHTACefiqzIGneW8wPYYgreJ738FVtHr3aMKZB963QZDZD"
act_id = "516894385544698"
secret = "-"
def getFacebookAPI(token, act_id, secret):
    token, act_id, secret
    if secret != '-':
        api = FacebookAdsApi.init(access_token=token, app_secret=secret)
    else:
        api = FacebookAdsApi.init(access_token=token)
        
    return api

def getInterestIDFromText(api, text):

#     print text.decode('utf-8')
    params = {
        'q': text,        
        'type': 'adinterest',
        'limit': 1000,        
    }
    resp = TargetingSearch.search(params=params, api=api)
    return resp

def getSuggestions(api, element):
    
    params = {
        'type': TargetingSearch.TargetingSearchTypes.interest_suggestion,
        'interest_list': [element],
        'limit':1000
    }
    
    resp = TargetingSearch.search(params=params, api=api)
    return resp

def validateInterestIdByInterest(api, list_interests): 
    params = {
        'type': 'adinterestvalid',
#             'interest_list': list_interests,
        'interest_fbid_list': list_interests,
    }
    resp = TargetingSearch.search(params=params, api=api)  
    return resp

# def getLocationElement(api, location_name, location_type='country'):        
#     responses = getLocations(location_name,api, location_type=location_type)
#     return resopn
# #     print responses
def getLocationElement(api, element, location_type="country"):
    
#     type=adgeolocation&location_types=['region']:   
    params = {
        'q': element,
        'type': 'adgeolocation',
#         'location_types': ['city'],
#         'location_types': ['region'],
        'location_types': [location_type],
#         'countries': ['US']
#         'match_country_code' :True 
    }
    responses = TargetingSearch.search(params=params)
    return responses



def findInterestByName(api, interest): 
    print ('**********  SEARCHING FOR %s  **********'  % interest)       
    search_result = getInterestIDFromText(api, interest)

    print ("interest_id: %s" % search_result[0]["id"])
  

def remote(interest):
    facebook_api = getFacebookAPI(token, act_id, secret)  
    search_result = getInterestIDFromText(facebook_api, interest)

    return search_result[0]["id"]


def main():
        
    facebook_api = getFacebookAPI(token, act_id, secret)   


if __name__ == "__main__":
    main()    
