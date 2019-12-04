# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
import sys
import json

#replace token and act_id with your value
token = "EAAbPAyrnxo0BAPzWuLX7rwvEQjsJqgapZB72uA3zPLY7JYwUFklwHHZAg5QDvntzLNejvpORZCVHnjS0aLyLZBGTl8qtiVh3oPB6Nz4TAonq2KxCv14Jsci5sja54rhDWOHTACefiqzIGneW8wPYYgreJ738FVtHr3aMKZB963QZDZD"
act_id = "516894385544698"
secret = "-"

#dictionary for global values
dict_demografics = {
    'total':230000000,
    'under 24' : 37000000,
    '25-34': 62000000,
    '35-44': 42000000,
    '45-54': 32000000,
    '55-64': 25000000,
    'over 65': 22000000,
    'african_american': 82000000,
    'asian_american':   4100000,
    'other': 120000000,
    'hispanic_all': 20000000,
    'college': 82901000,
    'high_school': 43000000,
    'grad_school':10580000, 
    'parents': 44000000, 
}
dict_demografics_percents = {}
for value in dict_demografics:
     dict_demografics_percents[value]= dict_demografics[value]/dict_demografics['total']

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
        "flexible_spec": [],
        'family_statuses':[]
          
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

education_status_grouped = {                                             
    'college':[2,3,5,6],
    "high_school":[1,4,13],
    'grad_school':[7,8,9,10,11],                  
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


def make_request_by_education (account, interest_id, education_status):
    grade_aux=0
    targeting_spec = get_default_targeting_spec()
    targeting_spec['interests'] = [interest_id]
    for grade in education_status:
        targeting_spec['education_statuses'] = [grade]        
        grade_aux += make_request(account,targeting_spec)
    audience = grade_aux
    return audience


def make_request_by_parents(account,interest_id):
    targeting_spec = get_default_targeting_spec()
    targeting_spec['interests'] = [interest_id]
    flexible_spec=[]
    flexible_spec.append({'family_statuses':[{'id':"6002714398372", "name":"Parents (All)"}]})
    targeting_spec['flexible_spec']=flexible_spec
    audience = make_request(account,targeting_spec)
    return audience          
   
def get_facebook_info(account ):
    
      
    interests = [6003336011256]
    
    
    for interest in interests:
# #         create new dictionaries to store audience values
        
        age_values = {}
        race_values = {}
        grade_values = {}
        parent_values ={}
        total_behaviors={}
        parents={}

        print ('Interest %s' % interest)
        
        ################################ AGE REQUEST #####################################
        total_age = 0
        for age_interval in age_intervals:
            valor  = make_request_by_age(account, interest, age_intervals[age_interval])
            total_age+=valor
            age_values[age_interval]= valor
        # print('\t%s'%age_values)
        total_behaviors["total_age"]=total_age
        
      #   # calculating percentages for age            
        for age_interval in age_values:
            age_values[age_interval]= ((age_values[age_interval]/total_behaviors["total_age"])/dict_demografics_percents[age_interval])

        print (age_values)                       
                                         
            
      #   ############################### RACE REQUEST ###########################################
        total_race = 0
        for race in racial_affinities:
            valor  = make_request_by_race(account, interest, race)
            #print('%s:%d' % (race, valor))
            total_race += valor
            race_values[race]= valor
        total_behaviors["total_race"]=total_race
      #   # calculating percentages for race            
        for race in race_values:
            race_values[race]= ((race_values[race]/total_behaviors["total_race"])/dict_demografics_percents[race])

        print (race_values)         

      # ############################### EDUCATION REQUEST ###########################################
        total_education = 0
        for grade in education_status_grouped:
            valor  = make_request_by_education(account, interest, education_status_grouped[grade])
            print('%s:%d' % (grade, valor))
            total_education += valor
            grade_values[grade]= valor
        total_behaviors["total_education"]=total_education
      #   # calculating percentages for education            
        for grade in grade_values:
            grade_values[grade]=((grade_values[grade]/total_behaviors["total_education"])/dict_demografics_percents[grade]) 

        print(grade_values)
############################### PARENTS REQUEST ###########################################
        total_parents  = make_request_by_parents(account, interest)
        print('Parents: %d' % ( total_parents))
        
        targeting_spec = get_default_targeting_spec()
        targeting_spec['interests'] = [interest]
        total_interest=make_request(account,targeting_spec)
        print('Total Public : %d' % total_interest)
        parent_values['parent'] = total_parents
        no_parents= total_interest - total_parents
        parent_values['no_parents']= no_parents
        print('No Parents: %d'% (no_parents)) 
        parents['parents']= (total_parents/total_interest)/dict_demografics_percents['parents']
        parents['no_parents']= (no_parents/total_interest)/(1 - dict_demografics_percents['parents'])
        print(parents)

    print(dict_demografics_percents)

        
def main(argv): 
    account = get_ad_account()
    get_facebook_info(account)    


if __name__ == "__main__":   
    main(sys.argv[1:])
    