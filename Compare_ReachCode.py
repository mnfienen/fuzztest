# This script is used to compare the nearest reachcode of a point with the pre-established group id
# to make sure that the distance analysis did not incorrectly group the points according to distance.


import numpy as np
import shapefile as shp
import os



# get site names, waterbody names, and site descriptions and force into tuple
def get_comparison_names():

    inshape = shp.Reader("buffer_intersect_new2")
    
    site_records = inshape.records()

    # create empty lists to hold site number, reachcode
    site_no = []
    reach_code = []

    for cr in  site_records:
        site_no.append(cr[-1])

    for cr in site_records:
        reach_code.append(cr[-3].rstrip())


    # zip all attributes lists into a tuple
    site_attributes_tuple = zip(site_no, reach_code)

    #empty dict
    site_attributes_dict = {}

    #tuple to dict with single groupID (key) and all reachcodes associated with the groupID (values)
    for key, value in site_attributes_tuple:
        site_attributes_dict.setdefault(key, []).append(value)

    return site_attributes_dict

    
#############
#MAIN
#############

# get the comparison names from the function
siteAttributes = get_comparison_names()

# get the first value for every groupID as a comparison value that will be used to check for matches among the other points in the group
primary_comparison = {}

for k,v in siteAttributes.iteritems():
    primary_comparison.setdefault(k, []).append(v[0])


# examines all the values per key by finding the length of each dictionary entry for each key,
# then checking to see if the comparison value exists in the entry.  If the entry exists it is popped off leaving only entries that do not match the search criteria
print "Points Flagged for followup (in ArcGIS SELECT query format) \n"

for k,v in siteAttributes.items():

    # get the dictionary entry length (number of points) at each key (groupID)
    entryLength = len(siteAttributes[k])-1

    i=0

    while i <= entryLength:
        # remove items that match
        if v[i] in primary_comparison[k]:
            siteAttributes.pop(k, v[i])
        # print out items that do not match the search criteria
        else:
            print """"projectID" = %s AND "REACHCODE" = '%s'""" %(k, v[i])

             
        i+=1
        

    
    


