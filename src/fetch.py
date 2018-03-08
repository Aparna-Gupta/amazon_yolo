from amazon_api import *
import json
from pprint import pprint

def retrive_data ( amazon_obj, asin_product_dict ) :
    for asin in asin_product_dict :
        data = get_data ( amazon_obj, asin )
        if data is None :
            continue
        description, rank = data
        asin_product_dict[ asin ]['description'] = description
        asin_product_dict[ asin ]['salesrank_2018'] = rank



def get_data ( amazon_obj, product_id ) :
    data = product_api ( amazon_obj, item_id = product_id )
    if data is None :
        print ( "Error : No product description" )
        return None
    #description, rank = data

    return data



if __name__ == '__main__' :
    raw_data_file = "../asinReviewDict.json"
    asin_product_dict = json.load ( open ( raw_data_file ) )
    #pprint(asin_product_dict)
    amazon_obj = authentication(  )
    retrive_data ( amazon_obj, asin_product_dict )
    
    with open('../asinReviewDict_modified.json', 'w') as outfile:
        json.dump(asin_product_dict, outfile)