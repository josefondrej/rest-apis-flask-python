from flask import Flask

print(__name__)

app = Flask(__name__)

stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]


# POST /store data: {name}
@app.route("/store", methods=["POST"])
def create_store():
    pass


# GET /store/<string:name>
@app.route("/store/<string:name>")  # http://127.0.0.1:5000/store/some_name (name variable will contain some_name
def get_store(name):
    pass


# GET /store
@app.route("/store")
def get_stores():
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/get_store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
