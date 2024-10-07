'''
Flask Application
'''
from dataclasses import asdict
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


@app.route('/resume/experience', methods=['GET', 'POST', 'PUT'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['experience']):
            return jsonify(data['experience'][index])
        return jsonify(data['experience'])

    if request.method == 'POST':
        request_data = request.get_json()
        new_experience = Experience(**request_data)
        data["experience"].append(new_experience)
        return jsonify(experience=asdict(new_experience), id=len(data) - 1), 201
    
    if request.method == 'PUT':
        request_data = request.get_json()
        experience_id = request_data["id"]

        # Ensure the experience list is large enough to accommodate the ID
        if experience_id >= len(data['experience']):
            return jsonify({"error": "Invalid ID"}), 404

        # Update the experience entry at the specified index
        updated_experience = Experience(**request_data['experience'])
        data['experience'][experience_id] = updated_experience

        return jsonify(id=experience_id, experience=updated_experience), 200

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST', 'DELETE', 'PUT'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
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

    if request.method == 'DELETE':
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
            deleted_education = data['education'].pop(index)
            return jsonify(deleted_education), 200

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST', 'PUT', 'DELETE'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
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

    if request.method == 'DELETE':
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
            deleted_skill = data['skill'].pop(index)
            return jsonify(deleted_skill), 200

    return jsonify({})
