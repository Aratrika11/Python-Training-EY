from flask import Flask,jsonify,request

app = Flask(__name__)
items = ["apple", "banana", "cherry"] #Database
# GET -> return full list
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)
#POST -> add a new item
@app.route("/items", methods=["POST"])
def add_items():
    data = request.get_json()
    item = data.get("item")
    items.append(item)
    return "POST EXECUTED"

#PUT -> update an item by index
@app.route("/items/<int:index>", methods=["PUT"])
def update_items(index):
    data = request.get_json()
    new_value = data.get("item")
    items[index] = new_value
    return "PUT EXECUTED"
#DELETE -> delete an item by index
@app.route("/items/<int:index>", methods=["DELETE"])
def delete_items(index):
    items.pop(index)
    return "DELETE EXECUTED"


if __name__ == "__main__":
    app.run()