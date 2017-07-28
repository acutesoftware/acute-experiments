#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config.py 
#
# Definitions and ontology to map area that is to be logged

areas = [
    {'name':'Bedroom', 'sensor_id':'br01'},
    {'name':'Lounge', 'sensor_id':'lounge'},
    {'name':'Kitchen', 'sensor_id':'kitchen'},
    {'name':'Hall', 'sensor_id':'hall'},
    {'name':'Garage', 'sensor_id':'garage'},
    {'name':'Front yard', 'sensor_id':'front'},
    {'name':'Back Yard', 'sensor_id':'back'},
    ]
    
people = [
    {'name':'YourName', 'id':'me'},
    {'name':'Frank', 'id':'primary_carer'},
    {'name':'Jane', 'id':'secondary_carer'},
    {'name':'Nick', 'id':'doctor'},
    ]

data_storage = [
    {'name':'Hard Drive', 'unc':'\\treebeard\c\files'},
    {'name':'NAS', 'unc':'\\fangorn\data\itnobam'},
    {'name':'Website', 'unc':'http://www.acutesoftware.com.au'},
    {'name':'Google Drive', 'unc':'https://drive.google.com/drive/'},
    ]
    
sensor_types = [
    {'name':'motion sensor', 'poll_frequency':'trigger'},
    {'name':'light sensor', 'poll_frequency':'1 minute'},
    {'name':'sound sensor', 'poll_frequency':'trigger'},
]    
    
    