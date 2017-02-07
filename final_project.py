from flask import Flask, render_template, request, redirect, url_for
from database import db_session
from models import Restaurant, MenuItem

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

# Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    restaurants = Restaurant.get_all()
    return render_template('all-restaurants.html', restaurants=restaurants)


@app.route('/restaurant/<int:restaurant_id>/')
def single_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    menu_items = MenuItem.get_by_restaurant_id(restaurant_id)
    return render_template('single-restaurant.html',
                           restaurant=restaurant,
                           menu_items=menu_items)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        Restaurant.create(restaurant_name)
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('new-restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/')
def edit_restaurant(restaurant_id):
    restaurant = restaurants[restaurant_id]
    return render_template('edit-restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/')
def delete_restaurant(restaurant_id):
    restaurant = restaurants[restaurant_id]
    return render_template('delete-restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def new_menu_item(restaurant_id):
    restaurant = restaurants[restaurant_id]
    return render_template('new-menu-item.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit/')
def edit_menu_item(restaurant_id, menu_item_id):
    restaurant = restaurants[restaurant_id]
    menu_item = items[menu_item_id]
    return render_template('edit-menu-item.html',
                           restaurant=restaurant,
                           menu_item=menu_item)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete/')
def delete_menu_item(restaurant_id, menu_item_id):
    restaurant = restaurants[restaurant_id]
    menu_item = items[menu_item_id]
    return render_template('delete-menu-item.html',
                           restaurant=restaurant,
                           menu_item=menu_item)

if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        SECRET_KEY='A Secret Key',
    )
    app.run(host='0.0.0.0', port=5000)
