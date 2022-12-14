"""
Generate keywords of products in an image
"""

from google.cloud import vision


def detect_text(content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts


def detect_logo(content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    logo = response.logo_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return logo


def detect_label(content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    label = response.label_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return label
