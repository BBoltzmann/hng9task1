from enum import Enum
from flask import *
import json, time
app = Flask(__name__)
@app.route('/', methods=['GET'])
def  home_page():
    userName  = 'Bboltzmann'
    age = 99
    backend = True
    bio = 'Hate me'
    data_set={"slackUsername":userName, "backend": backend, "age": age, "bio": bio }
    # json_dump = json.dumps(data_set)
    return data_set
@app.route('/calculator', methods=['POST'])
def  calculator():
    userName  = 'Bboltzmann'
    class OperationType(Enum):
        add  = 'addition'
        subtract = 'subtraction'
        multiply = 'multiplication'
    x  = request.json['x']
    y  = request.json['y']
    operation_type = request.json['operation_type']
    operation_slpit = operation_type.split()
    operation = [item.value for item in OperationType] 
    operation_id = [item.name for item in OperationType] 
    for data in operation_slpit: 
        if data in operation or data in operation_id:
            if data == 'addition' or 'add':
                result = x+y
                result = result
            elif data == 'subtraction' or 'subtract':
                result = x-y
            elif data == 'multiplication' or 'multiply':
                result = x*y
        data_set={"slackUsername":userName, "result": result, "operation_type":data }        
        # else:
        #     result = 'Please enter correct data'
        #     data_set={"slackUsername":userName, "result": result, "operation_type":'null' }

          
    return jsonify(data_set)




if __name__ == "__main__":
    app.run()