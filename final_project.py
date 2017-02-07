from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    return "This page shows all restaurants"


@app.route('/restaurant/<int:restaurant_id>/')
def single_restaurant(restaurant_id):
    return "This page displays a menu from one restaurant"


@app.route('/restaurant/new/')
def new_restaurant():
    return "This page creates a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit/')
def edit_restaurant(restaurant_id):
    return "This page edits a restaurant"


@app.route('/restaurant/<int:restaurant_id>/delete/')
def delete_restaurant(restaurant_id):
    return "This page deletes a restaurant"


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def create_menu_item(restaurant_id):
    return "This page creates a new menu item"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit/')
def edit_menu_item(restaurant_id, menu_item_id):
    return "This page edits a menu item"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete/')
def delete_menu_item(restaurant_id, menu_item_id):
    return "This page deletes a menu item"

if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        SECRET_KEY='A Secret Key',
    )
    app.run()
