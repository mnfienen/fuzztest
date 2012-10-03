import numpy as np
import shapefile as shp
import os
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



# get site names, waterbody names, and site descriptions and force into tuple
def get_comparison_names():

    inshape = shp.Reader("150m_buffer_intersect")
    
    
    comparison_records = inshape.records()

    # create empty lists to hold site names, waterbody names and site descriptions
    site_no = []
    site_names = []
    waterbody_names = []
    site_descriptions = []

    for cr in  comparison_records:
        site_no.append(cr[0])
        
    for cr in comparison_records:
            site_names.append(cr[2].lower())
    
    for cr in comparison_records:
        waterbody_names.append(cr[3].lower())

    for cr in comparison_records:
        site_descriptions.append(cr[6].lower().rstrip())

    # zip all 4 attributes lists into a tuple
    site_attributes_tuple = zip(site_no, site_names, waterbody_names, site_descriptions)

    print ".....Comparison Attributes from GIS Analysis Shapefile.....\n"
    print site_attributes_tuple



# get all stream names within watershed
def get_all_stream_names():

    inshape = shp.Reader("All_Watershed_streams_Dissol")

    stream_records = inshape.records()

    stream_names = []
    for cr in stream_records:
        stream_names.append(cr[0].lower())
            
    print "\n\n\n\n......All Stream Names in Watershed.....\n"
    print stream_names


#get all road names within watershed
def get_all_road_names():

    inshape = shp.Reader('All_BR_Watershed_roads_Disso')

    road_records = inshape.records()

    road_names = []
    for cr in road_records:
        road_names.append(cr[0].lower())

    print "\n\n\n\n.....All Road Names in Watershed......\n"
    print road_names
    return road_names

# ########
# MAIN
# ########

get_comparison_names()

get_all_stream_names()

rn = get_all_road_names()

testname = 'forest road 703'
fuzztest = []
for cn in rn:
	fuzztest.append(fuzz.ratio(cn,testname))
	
fuzztest = np.array(fuzztest)
maxrat = np.max(fuzztest)
indies = np.where(fuzztest == maxrat)
print '\n\n\n\n\n'
for i in indies[0]:
	print rn[i]


