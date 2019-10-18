import json


class Product(object):
    def __init__(self, id, common_name, description, price, img_url):
        self.id = id
        self.common_name = common_name
        self.description = description
        self.price = price
        self.img_url = img_url

    def price_str(self):
        return "%.2f ISK" % self.price

    def __repr__(self):
        return "<Product: %s, %s, %s>" % (self.id, self.common_name, self.price_str())


class Customer(object):
    def __init__(self, id, email, given_name, surname, telephone, tos_agree, address, region):
        self.id = id
        self.email = email
        self.given_name = given_name
        self.surname = surname

    def __repr__(self):
        return self.email


def get_products():
    with open('./app/static/projects/store/products.json') as f:
        products_obj = json.loads(f.read())

    products = []

    for product_obj in products_obj:
        product = Product(
            product_obj['id'],
            product_obj['title'],
            product_obj['description'],
            product_obj['price'],
            product_obj['image'])
        products.append(product)
    return products
