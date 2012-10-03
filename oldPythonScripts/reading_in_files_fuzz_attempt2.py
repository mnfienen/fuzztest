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



# print to test the squeezingly wheritude
np.set_printoptions(precision=2, suppress=True)
#print allrecords[0][np.squeeze(np.where(justfields=='site_descr'.lower()))-1]



# pull all the Comments

# first make an empty list for results
comments_only = []
for cr in allrecords:
    comments_only.append(cr[np.squeeze(np.where(justfields=='comments'.lower()))-1])



# use fuzzy ratio to compare nested string lists
def fuzz_it (fieldNames1, fieldNames2):

    for value in fieldNames1:
        for subvalue in fieldNames1:
            print subvalue[0], type(subvalue[0])
            fuzz.ratio(subvalue[0], subvalue[0])
            

            
            

            
           
            
            
        


    #for value in fieldNames1, fieldNames2:
        #for subvalue in fieldNames1, fieldNames2:
           #print subvalue[0][1][2]
        #print value, type(value)

        
            
 

def first_file_fields(allrecords):

    # pull all site descriptions
    site_description_only = []
    for cr in allrecords:
        site_description_only.append(cr[np.squeeze(np.where(justfields=='site_descr'.lower()))-1])

    # pull all site names
    site_name_only = []
    for cr in allrecords:
        site_name_only.append(cr[np.squeeze(np.where(justfields=='site_name'.lower()))-1])

    # pull all waterbodies
    waterbody_only = []
    for cr in allrecords:
        waterbody_only.append(cr[np.squeeze(np.where(justfields=='waterbody_'.lower()))-1])

    # nest up the field lists into a nice list of lists
    all_sites = zip(site_description_only, site_name_only, waterbody_only)
    for i in all_sites:
        print i

    

    #print len(all_sites),"ALL relevant fields"
    #print all_sites, type(all_sites)

    global fieldNames1
    fieldNames1 = all_sites

def second_file_fields(allrecords2):
    
    # pull all site descriptions
    site_description_only = []
    for cr in allrecords2:
        site_description_only.append(cr[np.squeeze(np.where(justfields=='site_descr'.lower()))-1])

    # pull all site names
    site_name_only = []
    for cr in allrecords2:
        site_name_only.append(cr[np.squeeze(np.where(justfields=='site_name'.lower()))-1])

    # pull all waterbodies
    waterbody_only = []
    for cr in allrecords2:
        waterbody_only.append(cr[np.squeeze(np.where(justfields=='waterbody_'.lower()))-1])

    # nest up the field lists into a nice list of lists
    all_sites = zip(site_description_only, site_name_only, waterbody_only)

    
    

    global fieldNames2
    fieldNames2 = all_sites

    fuzz_it(fieldNames1, fieldNames2)





first_file_fields(allrecords)
second_file_fields(allrecords2)











    
