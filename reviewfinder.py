import json
import math

import requests

from dotenv import load_dotenv
import os

load_dotenv()

YOUR_URL = os.getenv('REVIEW_API_URL')
YOUR_HOST = os.getenv('REVIEW_API_HOST')
YOUR_KEY = os.getenv('REVIEW_API_KEY')


def get_products(keyword: str):
    url = YOUR_URL
    headers = {
        "X-RapidAPI-Key": YOUR_KEY,
        "X-RapidAPI-Host": YOUR_HOST
    }
    querystring = {"domainCode": "ca", "keyword": keyword, "page": "1", "excludeSponsored": "false",
                   "sortBy": "relevanceblender"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)


def product_distance(text: list, product: list):
    """
    >>> t = ['a', 'b']
    >>> p = ['c' , 'd']
    >>> round(product_distance(t, p), 3)
    0.0
    """
    product_copy = product.copy()
    for i in range(len(text)):
        text[i] = ord(text[i].upper())
        product_copy[i] = ord(product_copy[i].upper())
    dot_product = sum(i[0] * i[1] for i in zip(text, product_copy))
    magnitude_text = math.sqrt(sum(i ** 2 for i in text))
    magnitude_product = math.sqrt(sum(i ** 2 for i in product_copy))

    return math.acos(dot_product / (magnitude_text * magnitude_product))


def get_best_description(product_descriptions: list, text_descriptions: list) -> int:
    """
    >>> pd = ['a green ball', 'on sale green frog', 'yellow school bus']
    >>> td = ['green', 'ball']
    >>> get_best_description(pd, td)
    0
    """
    i = 0
    curr_min = (0, -math.inf)
    for description in product_descriptions:
        new_desc = list(description)
        curr_sum = 0.0
        for text in text_descriptions:
            temp_text = list(text)
            temp_desc = new_desc
            while len(temp_text) < len(temp_desc):
                temp_text = temp_text + [' ']
            while len(temp_desc) < len(temp_text):
                temp_desc = temp_desc + [' ']
            curr_sum += product_distance(temp_text, temp_desc)

        if curr_sum / len(text_descriptions) > curr_min[1]:
            curr_min = (i, curr_sum / len(text_descriptions))
        i += 1

    return curr_min[0]


def get_rating(products, descriptions):
    best_desc_list = list(detail['productDescription'] for detail in products['searchProductDetails'])
    best_description = get_best_description(best_desc_list, descriptions)
    str_rating = products['searchProductDetails'][best_description]['productRating']

    final_str = ''
    for char in str_rating:
        if char == ' ':
            break
        final_str += char

    return float(final_str)

