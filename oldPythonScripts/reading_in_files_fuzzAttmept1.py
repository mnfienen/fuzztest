import numpy as np
import csv
import shapefile as shp
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



def parse_fields(allfields):
    # make an empty list
    fields_list = []
    # loop over the input fields list and pull out the names
    for cf in allfields:
        fields_list.append(cf[0].lower())
    
    # give back a list of just the names
    return np.array(fields_list)
    
    

#reader_input = csv.reader(open('glfwc_export.txt','rb'),delimiter = ',',quotechar='"')

# make a path that doesn't care if it's on windoze or a superior operating system like linux mac or anyone else
inpath = os.path.join('glfwc_experimental_shapefile','GLIFWC_points')
inpath2 = os.path.join('Fish_experimental_test_sites','wdnr_sites')

# make a shapefile object from the shapefile root name 
inshape = shp.Reader(inpath)
inshape2 = shp.Reader(inpath2)

# we can pull out various object properties
allfields = inshape.fields
allrecords = inshape.records()

allfields2 = inshape2.fields
allrecords2 = inshape2.records()

# yank out the FIELD NAMES ONLY from the crufty fields list
# call parse_fields function
justfields = parse_fields(allfields)
#print justfields
justfields2 = parse_fields(allfields2)




# print to test the squeezingly wheritude
np.set_printoptions(precision=2, suppress=True)
print allrecords[0][np.squeeze(np.where(justfields=='site_descr'.lower()))-1]



# pull all the Comments

# first make an empty list for results
comments_only = []
for cr in allrecords:
    comments_only.append(cr[np.squeeze(np.where(justfields=='comments'.lower()))-1])



# pull the near dist stuff and force into a float array
neardist_only = []
for cr in allrecords:
    neardist_only.append(cr[np.squeeze(np.where(justfields=='near_dist'.lower()))-1])

# pull all site descriptions
site_description_only = []
for cr in allrecords:
    site_description_only.append(cr[np.squeeze(np.where(justfields=='site_descr'.lower()))-1])
#print site_description_only


site_name_only2 = []
for cr in allrecords2:
    site_name_only2.append(cr[np.squeeze(np.where(justfields2=='site_name'.lower()))-1])
#print site_name_only2

   
# cast into a float array in numpy
neardist_only = np.array(neardist_only).astype(float)
np.set_printoptions(precision=2, suppress=True)
#print neardist_only

# or if you like other styles
#this does the same thing as casting
#neardist_only = np.array(neardist_only,dtype='float')
#np.set_printoptions(precision=2, suppress=True)
#print neardist_only

# print list of points where distance from stream is greater than 100m
def faraway_points(neardist_only):
    for i in neardist_only:
        if i > 100:
            print i


# print list of points with distance less than 100m
def nearby_points(neardist_only):
    for i in neardist_only:        
        if i < 100:
            print i
            print

# use fuzzy matching on fields
# only returns a nested list of string and match value
def extract_matches(site_description_only, site_name_only2):
    choices1 = site_description_only
    choices2 = site_name_only2

    #change the string to change the search criteria
    extractstring = "Javorski"
    print choices1
    print choices2
    print
    print

    fuzz_items1 = process.extract(extractstring, choices1, limit=2)
    fuzz_items2 = process.extract(extractstring, choices2, limit=1)
    
    print fuzz_items1[0]
    print fuzz_items2[0]

    #get_pointID(fuzz_items1, fuzz_items2, allrecords)

def get_pointID (fuzz_items1, fuzz_items2, allrecords):
    for cr in allfields:
        if 'site_descr' == fuzz_items1:
            print cr
        else: print 'ding'
    


extract_matches(site_description_only, site_name_only2)
#faraway_points(neardist_only)
#nearby_points(neardist_only)





    
