from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.Contractor

#collections
decks = db.decks   #currently whats  in stock
cart = db.cart     #collection of carts  for different users
ids = db.ids       #unique identifier so users dont mix carts

decks.drop()
cart.drop()
decks.insert_one({ 'img': "static/red.jpeg",  'description': 'Red Bicycle trading cards' })
decks.insert_one({ 'img': "static/blue.jpeg",  'description': 'Blue Bicycle trading cards' })
decks.insert_one({ 'img': "static/black.jpeg",  'description': 'Black Bicycle trading cards' })

app = Flask(__name__)

#Home page view, view all items for sale 
@app.route('/')
def index():
    return render_template('contract_index.html', decks=decks.find())

#view all item in carts
@app.route('/cart')
def viewCart():
    return render_template('contract_cart.html', cart=cart.find())

#adds a  new item to cart
@app.route('/add_to_cart/<deck_id>', methods=['POST'])
def addToCart(deck_id):
    item = decks.find_one({'_id': ObjectId(deck_id)})
    newItem = { 'img': item['img'], 'description': item['description'] }
    cart.insert_one(newItem) 
    return redirect(url_for('viewCart'))

#deletes an item from cart
@app.route('/cart/delete/<cart_id>', methods=['POST'])
def cartDeleteOne(cart_id):
    cart.delete_one({'_id': ObjectId(cart_id)})
    return redirect(url_for('viewCart'))

#user "checksout" and buys their stuff and empties cart
@app.route('/cart/checkout', methods=['POST'])
def cartDeleteAll():
    for item in cart.find():
        cart.delete_one(item)
    return render_template('contract_checkout.html')


if __name__ == '__main__':
    app.run(debug=True)