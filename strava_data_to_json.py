#!/usr/bin/python 

from pylab import *
import urllib.request
import json
import polyline
import os
os.getcwd()
# change working directory
os.chdir('/home/richard/Dropbox/Random_Stats_and_Big_Data/Python_stuff/Strava/Strava')
os.getcwd()
import richard_strava as rs


from imp import reload
reload(rs)

# import stravalib
response=urllib.request.urlopen('https://www.strava.com/api/v3/activities?access_token=91693b839810659899ca2514bfa9c24ab6040617')
data=response.read()
text=data.decode(encoding='utf-8') 
j_data=json.loads(text)

# get the data type
type(j_data)
# list

# get a list of the current valid attributes of an object
dir(j_data)


myrider=rs.Rider()
myrider.load_from_json_data(j_data)

# ideas for classes in this data
# ride 
# a class has methods that define its behavior



#decode polyline
poly_tran= polyline.decode(j_data[0]['map']['summary_polyline'])
poly_tran


# Lists are the "workhorse" datatype of Python

# Note: in Python- variables that store arrays always start with an @ character

# list manipulation

# get first listed achievement_count
j_data[0]['achievement_count']

# get the last achievement count 

# use a negative index in order to retrieve information from the end of the list
j_data[-1]['achievement_count']

# get all of the keys of a dictionary
j_data[0].keys()

# slicing a list
j_data[0]['achievement_count']

# create a list of achievement counts
achievment_counts = []

# append to the empty list
achievment_counts.append(j_data[0]['achievement_count'])

# note: lists are always seperated by commas
# note: lists can contain other lists

# values inside a list also called items 

# in python list indexing, the last value listed is not included in the returned sublist


# goal: get achievement_count, summary_polyline, distance, id, and start_date into a single list
# goal: subset the list j_data

# a list of lists
spam = [['cat','bat'], [10,20,30,40,50]]
spam[0]
spam[0][1]
spam[1][4]

len(j_data)
# 22 rides as of 06/06/16

# using for loops with lists
for i in range(len(j_data)):
    achievment_counts.append(j_data[i]['achievement_count'])
len(achievment_counts)
achievment_counts

# use multiple indexes to access lists of lists

# what about lists of dictionaries?
type(j_data[0])



#pylab stuff
poly_tran=array(poly_tran)
ion()

# this is using the figure object
ff=figure(45)

#use dir to view methods of figure

ff.clf()


#                                   color is black dots put on dot                 
plot(poly_tran[:,0],poly_tran[:,1],'k.-',linewidth=2)

#put grid on 
grid('off')

#aspect ratio
axis('equal')

xlabel('longitude')
ylabel('latitude')

show()






#use Stravalib
#client = stravalib.client.Client()
#client.access_token='91693b839810659899ca2514bfa9c24ab6040617'
#get list of athletes
#athlete=client.get_athlete('14036003')