from flask_cors import CORS
from flask import Flask, request, jsonify
import IssueController
import LoginController
#import AutotrasportatoreController



app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)



@app.route('/issue/newIssue', methods=['POST'])
def nuovaIssue():
    data = request.get_json()
    return IssueController.nuovaIssue(data)

@app.route('/issue/updateIssue', methods=['POST'])
def aggiornaIssue():
    data = request.get_json()
    return IssueController.aggiornaIssue(data)


@app.route('/issue/getIssue/<id>', methods=['GET'])
def ottieniIssue(id):
    result = IssueController.ottieniIssue(id)
    return jsonify(result)


@app.route('/issue/getAll', methods=['GET'])
def getAllIssue():
    return


@app.route('/autotrasportatore/getAutotrasportatore/<id>', methods=['GET'])
def getAutotrasportatoreId(id):
    #result = AutotrasportatoreController.ottieniAutotraportatoreById(id)
    #return jsonify(result)
    return




@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return LoginController.login(data["username"],data["password"])

app.run()