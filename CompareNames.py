import numpy as np
import shapefile as shp
import os
import re # regular expressions
import numpy as np # numpy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



# get site names, waterbody names, and site descriptions and force into tuple from a point shapefile of test sites
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

    #print ".....Comparison Attributes from GIS Analysis Shapefile.....\n"
    #for i in sorted(site_attributes_tuple):
        #print i

    return site_attributes_tuple

# get all stream names within watershed from a dissolved hydro shapefile
def get_all_stream_names():

    inshape = shp.Reader("All_Watershed_streams_Dissol")

    stream_records = inshape.records()

    stream_names = []
    for cr in stream_records:
        stream_names.append(cr[0].lower())
            
    return stream_names

#get all road names within watershed from a dissolved highway shapefile
def get_all_road_names():

    inshape = shp.Reader('All_BR_Watershed_roads_Disso')

    road_records = inshape.records()

    road_names = []
    for cr in road_records:
        road_names.append(cr[0].lower())

    return road_names


def fuzz_roadnames(roadn):
    #create empty lists for testing
    fuzztest = []
    fuzztestNoSP = []

    #loop through road names and append the fuzzy result to the fuzztest and NoSpace lists
    for cn in roadn:
            #testname lowercase
            fuzztest.append(fuzz.ratio(cn,testname))
            #testname without spaces
            fuzztestNoSP.append(fuzz.ratio(cn,testnameNoSP))

    # force ratio list results into a numpy array
    # find max ratio and indicies where max ratio exists
    fuzztest = np.array(fuzztest)
    maxrat = np.max(fuzztest)
    indies = np.where(fuzztest == maxrat)

    fuzztestNoSP = np.array(fuzztestNoSP)
    maxratNoSP = np.max(fuzztestNoSP)
    indiesNoSP = np.where(fuzztestNoSP == maxratNoSP)
    print '\n\n\n\n\nREGULAR TEST'
    for i in indies[0]:
            print roadn[i]
    print '\n\n\n\n\nNO SPACE TEST'
    
    for i in indiesNoSP[0]:
            print roadn[i]



def fuzz_roadnames_num_test(roadn):
    # fuzzy number test
    fuzztestNUM = []
    for cn in roadn:
            fuzztestNUM.append(fuzz.ratio(re.findall("\d+",cn),testnameNUM))
            fuzztestNUM.append(fuzz.ratio(cn,testnameNUM))

    fuzztestNUM = np.array(fuzztestNUM)
    maxratNUM = np.max(fuzztestNUM)
    indiesNUM = np.where(fuzztestNUM == maxratNUM)
    print '\n\n\n\n\nNUM TEST'
    for i in indiesNUM[0]:
            print roadn[i]




def fuzz_stream_names_test(streamn):
    fuzztest = []
    fuzztestNoSP = []

    for cn in streamn:
            fuzztest.append(fuzz.ratio(cn,streamTestName))
            fuzztestNoSP.append(fuzz.ratio(cn,streamTestNameNoSP))

    fuzztest = np.array(fuzztest)
    maxrat = np.max(fuzztest)
    indies = np.where(fuzztest == maxrat)
                                
    fuzztestNoSP = np.array(fuzztestNoSP)
    maxratNoSP = np.max(fuzztestNoSP)
    indiesNoSP = np.where(fuzztestNoSP == maxratNoSP)

    print '\n\n\n\n\n REGULAR STREAM NAME TEST'

    for i in indies[0]:
        print streamn[i]


# THIS WILL CHECK TO FIND sites that have been related spatially and compare fuzzy logic on the stream names
def compare_sites(pointAttributes, streamTestName):

    # get a list of the site IDs and find the max
    idList = []

    for item in pointAttributes:
        idList.append(item[0])
    maxIDnumber = max(idList)
    
 
    #Pseudo-code --> make an empty list, iterate through the point attributes by site ID number using the maximum point id number as a limiter
    #Pseudo-code --> if the point id number matches the current iteration number
    WaterbodyList = []
    IDNumberList = []
    streamTest = []

    j = 0
    k = 0
    while j <= maxIDnumber:
        for row in pointAttributes:
            if row[0] == j:
                WaterbodyList.append(row[2])
                WaterbodyList.append(fuzz.ratio(row[2], streamTestName))
                
                IDNumberList.append(row[0])
                #streamTest.append(fuzz.ratio(row[2],streamTestName))
            
        print WaterbodyList
        print IDNumberList
            
        #print streamTest
                
             
        j+= 1

        
    

    


   

    
    


    
    
        




# ########
# MAIN
# ########


# read in shapefile attributes site#, site name, waterbody, site description
pointAttributes = get_comparison_names()
#read in stream names from shapefile
streamn = get_all_stream_names()
#read in road names from shapefile
roadn = get_all_road_names()


# insert original road test name
testname = 'caroline'
# replace spaces with nothing
testnameNoSP = re.sub(' ','',testname)
#  return only numbers from testname
testnameNUM = re.findall("\d+",testname)

# insert original stream test name
streamTestName = 'tyler forks'
streamTestNameNoSP = re.sub(' ','',streamTestName)



#### run fuzzy tests
fuzz_roadnames(roadn)
#fuzz_roadnames_num_test(roadn)

fuzz_stream_names_test(streamn)

print "\n\n\n\nRESULTS FROM COMPAREPOINTS FUNCTION"
compare_sites(pointAttributes, streamTestName)
