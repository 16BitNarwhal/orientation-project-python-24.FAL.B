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
        return jsonify()

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

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
