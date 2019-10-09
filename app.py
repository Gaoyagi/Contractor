from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
controllers = db.controllers

app = Flask(__name__)

consoles = [
    { 'console': 'Xbox One', 'description': 'XBONE controllers' },
    { 'console': 'Playstation 4', 'description': 'PS4 Dual Shocks' },
    { 'console': 'Nintendo Switch', 'description': 'Joy Cons and Pro controllers' }
]

#Home page view 
@app.route('/')
def index():
    return render_template('contract_index.html', consoles = consoles)

# #ps5 controller page
# @app.route('/consoles/PS4/')
# def PSpage()
#     return render_template('contract_ps4.html')

#lets user order controllers we dont regularly, immedeityl goes to cart
@app.route('/controller/new')
def controller_new():
    return render_template('contract_new.html')

#posts the new console to  the database
@app.route('/controller', methods=['POST'])
def controller_submit():
    controller = {
        'console': request.form.get('console'),
        'controller': request.form.get('controller')
    }
    controllers.insert_one(controller)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)