import keywordcontroller

# print(keywordcontroller.get_review('redb.jpeg'))


def reviews(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    data = request.get_json()
    try:
        product_score = keywordcontroller.get_review(data['img_file'])
        return {"score": product_score}
    except Exception as e:
        return {
            'code': 'error',
            'message': str(e)
        }


