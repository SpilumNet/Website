from flask import Blueprint, render_template, session, redirect, flash

from . import model

bp = Blueprint('store', __name__)


@bp.route('/projects/store')
def index():
    obj = model.get_products()
    return render_template('projects/store/index.html', product_list=obj, title='Store')


@bp.route('/projects/store/<id>')
def product(id):
    products = model.get_products()
    for obj in products:
        if obj.id == id:
            return render_template('projects/store/product.html', product=obj)


@bp.route('/projects/store/cart')
def shopping_cart():
    if "cart" not in session:
        flash("There is nothing in your cart!")
        return render_template("projects/store/cart.html", display_cart={}, total=0)
    else:
        items = session["cart"]
        dict_of_products = {}

        total_price = 0
        products = model.get_products()
        for item in items:
            for obj in products:
                if obj.id == item:
                    product = obj
            total_price += product.price
            if product.id in dict_of_products:
                dict_of_products[product.id]["qty"] += 1
            else:
                dict_of_products[product.id] = {"qty": 1, "name": product.common_name, "price": product.price}
        return render_template("projects/store/cart.html", display_cart=dict_of_products, total=total_price)


@bp.route('/projects/store/add_to_cart/<id>')
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)

    flash("Successfully added to cart!")
    return redirect("/projects/store")


@bp.route('/projects/store/remove_from_cart/<id>')
def remove_from_cart(id):
    if "cart" not in session:
        return redirect("/projects/store/cart")
    else:
        session["cart"].remove(id)

    flash("Product removed from the cart!")
    return redirect("/projects/store/cart")


@bp.route("/projects/store/checkout")
def checkout():
    flash("Thank you for checking out my demo!")
    session["cart"] = {}
    return redirect("/projects/store/cart")
