import generatekeyword
import reviewfinder


def get_product_info(text_list, logo_list, label_info):
    for i in range(len(text_list)):
        text_list[i] = text_list[i].upper()
    for i in range(len(logo_list)):
        logo_list[i] = logo_list[i].upper()

    product_logos = []
    product_labels = []

    for item in logo_list:
        if item in text_list:
            product_logos.append(item)
    for item in label_info:
        if item.description.upper() in text_list:
            product_labels.append(item.description)

    if len(product_logos) > 5:
        return ' '.join(product_logos[:5])
    elif len(product_logos) > 0:
        return ' '.join(product_logos)
    elif len(product_labels) > 5:
        return ' '.join(product_labels[:5])
    elif len(product_labels) > 0:
        return ' '.join(product_labels)
    elif len(text_list) <= 5:
        return ' '.join(text_list)
    else:
        return ' '.join(text_list[:5])


def get_review(image):
    text_info = generatekeyword.detect_text(image)
    logo_info = generatekeyword.detect_logo(image)
    label_info = generatekeyword.detect_label(image)

    product_texts = text_info[0].description
    product_logos = logo_info[0].description
    text_list = str.split(product_texts, '\n')
    logo_list = str.split(product_logos, '\n')

    keywords = get_product_info(text_list, logo_list, label_info)

    online_products = reviewfinder.get_products(keywords)
    return reviewfinder.get_rating(online_products, text_list)