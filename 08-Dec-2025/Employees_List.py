from flask import Flask,jsonify,request

app = Flask(__name__)
employees = [{"id":1,"name":"Aratrika","role":"Developer"},
             {"id":2,"name":"Nirakshi","role":"Architect"}]

#GET all employees
@app.route("/get-emp", methods=["GET"])
def get_emp():
    return jsonify(employees)

#GET employee by ID
@app.route("/get-emp/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp)
    return jsonify({"message":"Employee not found"}),404

#POST
@app.route("/create-emp", methods=["POST"])
def create_emp():
    new_emp = request.get_json()
    employees.append(new_emp)
    return jsonify({"message":"Employee created", "employee":new_emp}),201

#PUT
@app.route("/update-emp/<int:emp_id>", methods=["PUT"])
def update_emp(emp_id):
    new_data = request.get_json()
    for emp in employees:
        if emp["id"] == emp_id:
            emp.update(new_data)
            return jsonify({"message":"Employee updated", "employee":emp}),200
    return jsonify({"message":"Employee not found"}),404

#DELETE
@app.route("/delete-emp/<int:emp_id>", methods=["DELETE"])
def delete_emp(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            return jsonify({"message":"Employee deleted"}),200
    return jsonify({"message":"Employee not found"}),404

if __name__ == "__main__":
    app.run()