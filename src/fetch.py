from amazon_api import *
import json
from pprint import pprint

DELAY = .5    # taaki Amazon danda naa maare

'''
It will iterate through all the 2014 data entries and retrieve latest 2018 product data
from Amazon API and add it back to the data

'''
def iter_retrive_data ( amazon_obj, asin_product_dict ) :
    asin_not_found_list = []
    for index, asin in enumerate ( asin_product_dict ) :
        print ( " {} ASIN : {}".format ( index, asin  )  )
        util_delay ( DELAY )
        data = get_data ( amazon_obj, asin )
        if data is None :
            continue
        elif data is ASIN_ERROR :
            asin_not_found_list.append ( asin )
            continue
        description, rank = data
        asin_product_dict[ asin ]['description'] = description
        asin_product_dict[ asin ]['salesrank_2018'] = rank
        # pprint ( asin_product_dict[ asin ] )

    for asin in asin_not_found_list :
        del asin_product_dict[ asin ]
        print( "Deleted entry for asin not found" )


def get_data ( amazon_obj, product_id ) :
    data = product_api ( amazon_obj, item_id = product_id )
    if data is None or data is ASIN_ERROR:   # TODO do something with ASIN not found
        print ( "Error : No product description" )
        return data
    #description, rank = data

    return data



if __name__ == '__main__' :
    raw_data_file = "../asinReviewDict.json"
    asin_product_dict = json.load ( open ( raw_data_file ) )
    #pprint(asin_product_dict)
    amazon_obj = authentication(  )
    iter_retrive_data ( amazon_obj, asin_product_dict )
    
    with open('../asinReviewDict_v2_modified.json', 'w') as outfile:
        json.dump(asin_product_dict, outfile)