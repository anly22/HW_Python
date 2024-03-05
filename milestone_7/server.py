from flask import Flask, jsonify, request
import csv
import utils

app = Flask(__name__)

DB = []
with open('database.csv') as file: # filename = database.csv
    reader = csv.DictReader(file, delimiter=",")
    
    headers = next(reader)
    for col in reader:
        DB.append(col)


@app.route("/birthdays")
def birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    if month and department:
        res_b_data = utils.count_by_id(DB,'birth_date', month, "birthday", department)
        if res_b_data:
            return jsonify(res_b_data), 200
        else:
            return jsonify({'message': 'No result for entered parameters'}), 404
    else:
        return jsonify({'message': 'Please provide month and department parameters'}), 400


@app.route("/anniversaries") 
def anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    if month and department:
        res_a_data = utils.count_by_id(DB, 'hiring_date', month, "anniversary", department)
        if res_a_data:
            return jsonify(res_a_data), 200
        else:
            return jsonify({'message': 'No result for entered parameters'}), 404
    else:
        return jsonify({'message': 'Please provide month and department parameters'}), 400


if __name__ == '__main__':
    app.run(debug=True)