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
        "geo_locations": {"countries":["US"], 'location_types': ['home'],},
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
genders = {          
    'male': [1],
    'female': [2]
}

age_intervals = {            
    'under 24' :{'age_min': 13, 'age_max': 24},
    '25-34':{'age_min':25,'age_max':34},
    '35-44':{'age_min':35,'age_max':44},
    '45-54':{'age_min':45,'age_max':54},
    '55-64':{'age_min':55,'age_max':64},
    'over 65':{'age_min':65,'age_max':-1},                         
}

racial_affinities = {                     
    'african_american': {"id":"6018745176183","name":"African American (US)"},
    'asian_american': {"id":"6021722613183","name":"Asian American (US)"},
    'hispanic_all': {"id":"6003133212372","name":"Hispanic (US - All)"},
    'other': 'dealt with specially' #excluded
    # this goes into behaviors in exclusions     
}

caucasian_spec = {
    "behaviors":[
        {"id":"6018745176183","name":"African American (US)"},
        {"id":"6021722613183","name":"Asian American (US)"},
        {"id":"6003133212372","name":"Hispanic (US - All)"}
    ]
}

income_levels={
#         'all': [],
#         'all': [],
    '30k_to_40k':[{"id": "6018510070532","name": "$30,000 - $40,000"}],                 
    '40k_to_50k':[{"id": "6018510087532","name": "$40,000 - $50,000"}],
    '50k_to_75k':[{"id": "6018510122932","name": "$50,000 - $75,000"}],        
    '75k_to_100k':[{"id": "6018510100332","name": "$75,000 - $100,000"}],
    '100k_to_125k':[{"id": "6018510083132","name": "$100,000 - $125,000"}],
    '125k_to_150k':[{"id": "6017897162332","name": "$125,000 - $150,000"}],
    '150k_to_250k':[{"id": "6017897374132","name": "$150,000 - $250,000"}],
    '250k_to_350k':[{"id": "6017897397132","name": "$250,000 - $350,000"}], 
    '350k_to_500k':[{"id": "6017897416732","name": "$350,000 - $500,000"}],
    'over_500k':[{"id": "6017897439932","name": "Over $500,000"}]                                                            
}
     

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
    return audience  
    
    
def make_request_by_age(account, interest_id, age_interval):
    targeting_spec = get_default_targeting_spec()    
    targeting_spec['interests'] = [interest_id]
    targeting_spec['age_min']=age_interval['age_min']
    if 'age_max' in targeting_spec:                                
        del targeting_spec['age_max']     
    if (age_interval['age_max'] != -1):
        targeting_spec['age_max']= age_interval['age_max']  
    audience = make_request(account,targeting_spec)
    return audience  

def make_request_by_race (account, interest_id, race):
    targeting_spec = get_default_targeting_spec()
    targeting_spec['interests'] = [interest_id]
    
    if race == 'other':
        exclusion_race = caucasian_spec['behaviors']
        targeting_spec['exclusions'] = {'behaviors': exclusion_race}
    else:
        targeting_spec['flexible_spec'] = [{'behaviors': [racial_affinities[race]]}]
    audience = make_request(account,targeting_spec)
    return audience

          
   
def get_politicians_distribution(account):
    #dictionaries with the possible values for the attributes gender and age intervals
    genders = {          
        'male': [1],
        'female': [2]
    }
    
    age_intervals = {            
        'under 24' :{'age_min': 13, 'age_max': 24},
        '25-34':{'age_min':25,'age_max':34},
        '35-44':{'age_min':35,'age_max':44},
        '45-54':{'age_min':45,'age_max':54},
        '55-64':{'age_min':55,'age_max':64},
        'over 65':{'age_min':65,'age_max':-1},                         
    }
    
    racial_affinities = {                     
        'african_american': {"id":"6018745176183","name":"African American (US)"},
        'asian_american': {"id":"6021722613183","name":"Asian American (US)"},
        'hispanic_all': {"id":"6003133212372","name":"Hispanic (US - All)"},
        'other': 'dealt with specially' #excluded
        # this goes into behaviors in exclusions     
    }
    
    caucasian_spec = {
        "behaviors":[
            {"id":"6018745176183","name":"African American (US)"},
            {"id":"6021722613183","name":"Asian American (US)"},
            {"id":"6003133212372","name":"Hispanic (US - All)"}
        ]
    } 
      
    politicians_interest = ["6003257632086","6003485071480","6003124160217","6002878910972"]
    
    
    for politician_interest in politicians_interest:
#         create new dictionaries to store audience values
        gender_values = {}
        age_values = {}
        race_values = {}
        
        print ('politician %s' % politician_interest)
        ########################## GENDER REQUEST ################################
        total_gender = 0
        for gender in genders:
            valor  = make_request_by_gender(account, politician_interest, genders[gender])
            total_gender+=valor
            gender_values[gender]= valor # create a key in the dictionary and store the value. 
             
        print ('\t%s'% gender_values) # check the created dict values.
            
        # calculating percentages for gender
        for gender in gender_values:
            print ('\tpercentage of %s: %.2f' % (gender, (float(gender_values[gender])/total_gender)*100))
        
        ################################ AGE REQUEST #####################################
        total_age = 0
        for age_interval in age_intervals:
            valor  = make_request_by_age(account, politician_interest, age_intervals[age_interval])
            total_age+=valor
            age_values[age_interval]= valor

        # calculating percentages for age            
        for age_interval in age_values:
            print ('\tpercentage of %s: %.2f' % (age_interval, (float(age_values[age_interval])/total_age)*100))                       
                                         
            
        ############################### RACE REQUEST ###########################################
        total_race = 0
        for race in racial_affinities:
            valor  = make_request_by_race(account, politician_interest, race)
            print('%s:%d' % (race, valor))
            total_race += valor
            race_values[race]= valor

        # calculating percentages for race            
        for race in race_values:
            print ('\tpercentage of %s: %.2f' % (race, (float(race_values[race])/total_race)*100))   

        
def main(argv): 
    account = get_ad_account()
    get_politicians_distribution(account)    


if __name__ == "__main__":   
    main(sys.argv[1:])
