from amazon_api import *

def retrive_data ( amazon_obj, asin_product_dict ) :
    for asin in asin_product_dict :
        data = get_data ( amazon_obj, asin )
        if data is None :
            continue
        description, rank = data
        asin_product_dict[ asin ]['description'] = description
        asin_product_dict[ asin ]['salesrank'] = rank



def get_data ( amazon_obj, product_id ) :
    data = product_api ( amazon_obj, item_id = product_id )
    if data is None :
        print ( "Error : No product description" )
        return None
    #description, rank = data

    return data



if __name__ == '__main__' :
    amazon_obj = authentication(  )
    retrive_data ( amazon_obj, asin_product_dict )
