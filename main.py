
from crypt import methods
from flask import *
import json, time


app = Flask(__name__)

@app.route('/', methods=['GET'])
def  home_page():
    data_set={"slackUsername":'Bboltzmann', "backend": 'true', "age": 99, "bio": 'Hate me' }
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/user/', methods=['GET'])
def  request_page():
    user_query = str(request.args.get('user')) #/user/?user=bboltzmann

    data_set={"Page":'Request', "Message": f'Successfully got the request for {user_query}', 'time':time.time() }
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == "__main__":
    app.run()