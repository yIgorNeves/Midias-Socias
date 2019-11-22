# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
import sys

#replace token and act_id with your value
token = "EAAbPAyrnxo0BAPzWuLX7rwvEQjsJqgapZB72uA3zPLY7JYwUFklwHHZAg5QDvntzLNejvpORZCVHnjS0aLyLZBGTl8qtiVh3oPB6Nz4TAonq2KxCv14Jsci5sja54rhDWOHTACefiqzIGneW8wPYYgreJ738FVtHr3aMKZB963QZDZD"
act_id = "516894385544698"
secret = "-"


# https://developers.facebook.com/docs/marketing-api/targeting-search/

def get_default_targeting_spec():
    targeting_spec = {
        "geo_locations": {"countries":["BR"], 'location_types': ['recent', 'home'],},
    #     "geo_locations": {"countries":["US"], 'location_types': ['home']},
        "publisher_platforms": ["facebook", "instagram"],
        "facebook_positions": ["feed", "instream_video"], #feed, right_hand_column
    #     "device_platforms": ["mobile", "desktop"],
        "excluded_publisher_categories": [],
        "excluded_publisher_list_ids": [],
        "user_device": [],
        "excluded_user_device": [],
        "user_os": [],
        "wireless_carrier": [],
        'behaviors': [],
        'interests': [],
        "flexible_spec": []        
    } 
    return targeting_spec   

def get_ad_account():
    
    if secret != '-':
        FacebookAdsApi.init(access_token=token, app_secret=secret, api_version='v4.0')
    else:
        FacebookAdsApi.init(access_token=token, api_version='v4.0')
    account = AdAccount('act_' + act_id)
    return account


def make_request(account, targeting_spec):
    api_params = {
        'targeting_spec': targeting_spec
    }
    
    reach_estimate = account.get_reach_estimate(params=api_params)
    number = reach_estimate[0]['users']
    return number


def make_request_by_gender(account, interest_id, gender):
    targeting_spec = get_default_targeting_spec()
    targeting_spec['interests'] = [interest_id]
    targeting_spec['genders'] = gender   
    audience = make_request(account,targeting_spec)
#     print 'audience_size: %d' % audience
    return audience  
    
    
def make_request_by_age(account, interest_id, age_interval):
    targeting_spec = get_default_targeting_spec()    
    targeting_spec['interests'] = [interest_id]
    print (age_interval)
    targeting_spec['age_min']=age_interval['age_min']
    if 'age_max' in targeting_spec:                                
        del targeting_spec['age_max']     
    if (age_interval['age_max'] != -1):
        targeting_spec['age_max']= age_interval['age_max']  
    audience = make_request(account,targeting_spec)
#     print 'audience_size: %d' % audience
    return audience  
          
   
def get_politicians_distribution(account):
    #dictionaries with the possible values for the attributes gender and age intervals
    genders = {          
        'male': [1],
        'female': [2]
    }
    
    age_intervals = {            
        'adolescent' :{'age_min': 13, 'age_max': 17},
        'young' :{'age_min': 18, 'age_max': 39},
        'old': {'age_min': 40, 'age_max':-1}                                  
    }
    
    racial_affinities = {                     
        'african_american': {"id":"6018745176183","name":"African American (US)"},
        'asian_american': {"id":"6021722613183","name":"Asian American (US)"},
        'hispanic_all': {"id":"6003133212372","name":"Hispanic (US - All)"},
        #'other': 'dealt with specially' #excluded
        # this goes into behaviors in exclusions     
    }
    
    caucasian_spec = {
        "behaviors":[
            {"id":"6018745176183","name":"African American (US)"},
            {"id":"6021722613183","name":"Asian American (US)"},
            {"id":"6003133212372","name":"Hispanic (US - All)"}
        ]
    } 
    
        
    
    # 6003280320043 -  Fernando Haddad
    # 6013219668741 - Jair Bolsonaro
    
    # 6003210792176 -  Donald Trump
    # 6003361373387 - Hillary Clinton   
    politicians_interest = ["6003210792176","6003361373387"]
    
    
    for politician_interest in politicians_interest:
#         create new dictionaries to store audience values
        gender_values = {}
        age_values = {}
        
        print ('politician %s' % politician_interest)
        
        total_gender = 0
        for gender in genders:
            valor  = make_request_by_gender(account, politician_interest, genders[gender])
            total_gender+=valor
            gender_values[gender]= valor # create a key in the dictionary and store the value. 
             
        print ('\t%s'% gender_values) # check the created dict values.
            
        # calculating percentages for gender
        for gender in gender_values:
            print ('\tpercentage of %s: %.2f' % (gender, (float(gender_values[gender])/total_gender)*100))
            
        
        total_age = 0
        for age_interval in age_intervals:
            valor  = make_request_by_age(account, politician_interest, age_intervals[age_interval])
            total_age+=valor
            age_values[age_interval]= valor

        # calculating percentages for gender            
        for age_interval in age_values:
            print ('\tpercentage of %s: %.2f' % (age_interval, (float(age_values[age_interval])/total_age)*100))                       
                     
    
    
def main(argv): 
    account = get_ad_account()
    get_politicians_distribution(account)    


if __name__ == "__main__":   
    main(sys.argv[1:])
