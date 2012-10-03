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

# make a shapefile object from the shapefile root name 
inshape = shp.Reader(inpath)

# we can pull out various object properties
allfields = inshape.fields
allrecords = inshape.records()

# yank out the FIELD NAMES ONLY from the crufty fields list
# call parse_fields function
justfields = parse_fields(allfields)
print justfields



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


   
# cast into a float array in numpy
neardist_only = np.array(neardist_only).astype(float)
np.set_printoptions(precision=2, suppress=True)
print neardist_only

# or if you like other styles
#this does the same thing as casting
#neardist_only = np.array(neardist_only,dtype='float')
#np.set_printoptions(precision=2, suppress=True)
#print neardist_only

def faraway_points(neardist_only):
    for i in neardist_only:
        if i > 100:
            print i



def nearby_points(neardist_only):
    for i in neardist_only:        
        if i < 100:
            print i
            print






faraway_points(neardist_only)
nearby_points(neardist_only)





    
