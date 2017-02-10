from flask import Flask, render_template, request, redirect, url_for, \
    jsonify, flash
from database import db_session
from models import Restaurant, MenuItem

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    restaurants = Restaurant.get_all()
    return render_template('all-restaurants.html', restaurants=restaurants)


@app.route('/restaurants/JSON/')
def all_restaurans_JSON():
    restaurants = Restaurant.get_all()
    return jsonify(restaurants=[r.serialize for r in restaurants])


@app.route('/restaurant/<int:restaurant_id>/')
def single_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    menu_items = MenuItem.get_by_restaurant_id(restaurant_id)
    return render_template('single-restaurant.html',
                           restaurant=restaurant,
                           menu_items=menu_items)


@app.route('/restaurant/<int:restaurant_id>/menu/JSON/')
def single_restaurant_JSON(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    menu_items = MenuItem.get_by_restaurant_id(restaurant_id)
    return jsonify(menu_items=[i.serialize for i in menu_items])


@app.route('/restaurant/new/',
           methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        Restaurant.create(restaurant_name)
        flash('New restaurant created')
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('new-restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/',
           methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        restaurant.update(name=restaurant_name)
        flash('Restaurant edited')
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('edit-restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/',
           methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    if request.method == 'POST':
        restaurant.delete()
        flash('Restaurant deleted')
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('delete-restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/new/',
           methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        menu_item_name = request.form['menu_item_name']
        menu_item_description = request.form['menu_item_description']
        menu_item_price = request.form['menu_item_price']
        MenuItem.create(
            name=menu_item_name,
            description=menu_item_description,
            price=menu_item_price,
            restaurant_id=restaurant_id
        )
        flash('New menu item created')
        return redirect(url_for('single_restaurant',
                                restaurant_id=restaurant_id))
    else:
        restaurant = Restaurant.get_by_id(restaurant_id)
        return render_template('new-menu-item.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/JSON/')
def single_menu_item_JSON(restaurant_id, menu_item_id):
    menu_item = MenuItem.get_by_id(menu_item_id)
    return jsonify(menu_item=menu_item.serialize)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit/',
           methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_item_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    menu_item = MenuItem.get_by_id(menu_item_id)
    if request.method == 'POST':
        menu_item_name = request.form['menu_item_name']
        menu_item_description = request.form['menu_item_description']
        menu_item_price = request.form['menu_item_price']
        menu_item.update(
            name=menu_item_name,
            description=menu_item_description,
            price=menu_item_price
        )
        flash('Menu item edited')
        return redirect(url_for('single_restaurant',
                                restaurant_id=restaurant_id))
    else:
        return render_template('edit-menu-item.html',
                               restaurant=restaurant,
                               menu_item=menu_item)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete/',
           methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_item_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    menu_item = MenuItem.get_by_id(menu_item_id)
    if request.method == 'POST':
        menu_item.delete()
        flash('Menu item deleted')
        return redirect(url_for('single_restaurant',
                                restaurant_id=restaurant.id))
    else:
        return render_template('delete-menu-item.html',
                               restaurant=restaurant,
                               menu_item=menu_item)

if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        SECRET_KEY='A Secret Key',
    )
    app.run(host='0.0.0.0', port=5000)
