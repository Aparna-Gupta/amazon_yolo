import glob
import json
from pprint import pprint


# For merging data retrieved from API with data from dataset dumped as json

if __name__ == '__main__' :
    raw_data_file = "../asinReviewDict.json"
    asin_product_dict = json.load ( open ( raw_data_file ) )

    directory = "../"
    file_prefix = "partial"
    files  = glob.glob( directory + "partial-*.json" )
    for name in files :
        asin_new_data = json.load ( open ( name ) )
        for asin in asin_new_data :
            # pprint( asin_new_data[asin] )
            description = asin_new_data [ asin ]['description']
            salesrank_2018 = asin_new_data [ asin ]['salesrank_2018']
            asin_product_dict[ asin ][ 'description' ] = description
            asin_product_dict[ asin ][ 'salesrank_2018' ] = salesrank_2018

    incomplete_asins = []
    for asin in asin_product_dict :
        if 'salesrank_2018' not in asin_product_dict[asin] :
            # pprint(asin_product_dict[asin])
            incomplete_asins.append( asin )

    for asin in incomplete_asins :
        pprint("deleting asin " + asin )
        del asin_product_dict[ asin ]

    pprint( "Final list length {}".format(len(asin_product_dict) ))

    with open('../asinReviewDict_v2_modified.json', 'w') as outfile:
        json.dump(asin_product_dict, outfile)