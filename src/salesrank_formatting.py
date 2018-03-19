from pprint import pprint
import json
if __name__ == '__main__' :
    
    out_sales_json = {}

    raw_data_file = "../SalesData.txt"
    with open( raw_data_file ) as f :
        temp_list = []
        for line in f :
            temp_list.append( line )
            if( len( temp_list ) == 3 ) :
                asin = temp_list[ 0 ].strip()
                salesrank = temp_list[ 1 ].strip()
                sales = temp_list[ 2 ].replace(",", "").replace("<", "").replace(">", "").strip()
                try :
                    sales = int(sales)
                except:
                    pprint(sales)
                    temp_list = [] #empty it
                    continue
                out_sales_json[ asin ] = {"salesrank" : salesrank, "sales": sales}
                temp_list = [] #empty it
    pprint( "Final dict length {}".format(len(out_sales_json) ))

    with open('../out/sales.json', 'w') as outfile:
        json.dump(out_sales_json, outfile)