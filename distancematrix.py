# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:17:22 2021

@author: levir
"""

import requests



def distance(distance1):
    try:
        adress="תל אביב"
        api_key="AIzaSyA88C01yA6mRGbohjbbuAPr8ZzpgQsEPJU"
       
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(adress,distance1,api_key)
        res=requests.get(url).json()
       
        url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(distance1,api_key)
        res2=requests.get(url2).json()
        
        distance2 = res['rows'][0]['elements'][0]['distance']['text']
        duration = res['rows'][0]['elements'][0]['duration']['text']
        latitude = res2['results'][0]['geometry']['location']['lat']
        longitude = res2['results'][0]['geometry']['location']['lng']
        
        City_details = (distance2, duration) + (latitude, longitude) 
        City_destinations[distance1] = City_details
    
    except:
        print(" הערך" + distance1 + "לא מזוהה")
City_destinations=dict()
   
def place ():
    file= open("dests.txt",encoding="utf8")
    destination=list()
    for line in file:
            destination.append(line.strip()) 
    dest_len=len(destination)
    print("")
    print("מידע עבור כל יעד:")
    for i in range(dest_len):
        distance(destination[i]) 
    print(City_destinations)
    distance_list=list()
    
    for k,v in City_destinations.items():
        distance_list.append((v[0],k))
    distance_list.sort()
    
    print("")
    print("שלושת הערים הכי רחוקות מתל אביב הן:")
    distance_list=distance_list[-3:]
    
    for i in distance_list:
        print(i)

place()
