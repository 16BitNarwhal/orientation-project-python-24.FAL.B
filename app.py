'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index and 0 <= index < len(data['experience']):
            return jsonify(data['experience'][index])
        return jsonify(data['experience'])

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST', 'PUT'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index and 0 <= index < len(data['education']):
            return jsonify(data['education'][index])
        return jsonify(data['education'])

    if request.method == 'POST':
        return jsonify({})

    if request.method == 'PUT':
        request_data = request.get_json()
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
            updated_education = Education(**request_data)
            data['education'][index] = updated_education
            return jsonify(id=index, experience=updated_education), 200
        return jsonify({"error": "Invalid ID"}), 404

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST', 'PUT'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index and 0 <= index < len(data['skill']):
            return jsonify(data['skill'][index])
        return jsonify(data['skill'])

    if request.method == 'POST':
        return jsonify({})

    if request.method == 'PUT':
        request_data = request.get_json()
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
            updated_skill = Education(**request_data)
            data['skill'][index] = updated_skill
            return jsonify(id=index, experience=updated_skill), 200
        return jsonify({"error": "Invalid ID"}), 404

    return jsonify({})
