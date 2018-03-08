#!/bin/python3

# @author pratikone 


from amazon.api import AmazonAPI
from bs4 import BeautifulSoup
# Needs lxml parser as dependency for BeautifulSoup


def authentication ( ) :
    amazon_key = "AKIAIJT73X7ECP7STIRQ"
    amazon_secret = "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"
    amazon_tag = "mobilead0fcd2-20"
    amazon = AmazonAPI ( amazon_key, amazon_secret, amazon_tag )
    return amazon

def util_print_products ( products ) :
    for i, product in enumerate(products):
        print ("{0}. '{1} {2}'".format(i, product.asin, product.title) )

def product_api ( amazon_obj, item_id  ):
    product = amazon_obj.lookup(ItemId= item_id)
    if len ( product.editorial_reviews ) < 0 :
        print ( "Error: No editorial review" )
        return None
    soup = BeautifulSoup(product.editorial_reviews[0], "lxml")
    # print ( "Title ", product.title )
    # print ( "Description in html \n", soup.get_text())
    # print ( "sales rank ", product.sales_rank )

    return ( soup.get_text(), product.sales_rank )


def lookup_api ( amazon_obj, search_term ) :
    products = amazon_obj.search(Keywords = search_term, SearchIndex='All')  # search_n(n, ....) for first n results
    util_print_products ( products )

def similarity_lookup ( amazon_obj, products_ids ) :
    products = amazon_obj.similarity_lookup(ItemId = products_ids )    #ItemId = 'B0051QVESA,B005DOK8NW'
    util_print_products ( products )


if __name__ == '__main__' :
    amazon_obj = authentication(  )
    print (product_api ( amazon_obj, item_id = 'B00K7VZ138' ))
    #lookup_api ( amazon_obj, "toothbrush"  )
    #similarity_lookup ( amazon_obj, 'B00K7VZ138' )
    