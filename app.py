'''
Flask Application
'''
from dataclasses import asdict
from typing import List, Dict, Any
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

def validate_fields(required_fields: List[str], request_data: Dict[str, Any]) -> tuple:
    '''
    Validate that all the required fields are present in the request data
    '''
    missing_fields = [field for field in required_fields if field not in request_data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, ""

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
        if index is not None and 0 <= index < len(data['experience']):
            return jsonify(data['experience'][index])
        return jsonify(data['experience'])

    if request.method == 'POST':
        request_data = request.get_json()
        required_fields = ["title", "company", "start_date", "end_date", "description", "logo"]
        is_valid, error_mssg = validate_fields(required_fields, request_data)

        if not is_valid:
            return jsonify({"error": error_mssg}), 400

        try:
            new_experience = Experience(**request_data)
            data["experience"].append(new_experience)
            return jsonify(experience=new_experience, id=len(data['experience'])-1), 201
        except TypeError as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({}), 405

@app.route('/resume/education', methods=['GET', 'POST', 'DELETE', 'PUT'])
def education():
    '''
    Handles education requests
    '''

    def handle_get():
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
            return jsonify(data['education'][index])
        return jsonify(data['education'])

    def handle_post():
        request_data = request.get_json()
        required_fields = ["course", "school", "start_date", "end_date", "grade", "logo"]
        is_valid, error_mssg = validate_fields(required_fields, request_data)

        if not is_valid:
            return jsonify({"error": error_mssg}), 400
        try:
            new_education = Education(**request_data)
            data["education"].append(new_education)
            return jsonify(education=new_education, id=len(data['education'])-1), 201
        except TypeError as e:
            return jsonify({"error": str(e)}), 400

    def handle_put():
        request_data = request.get_json()
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
            updated_education = Education(**request_data)
            data['education'][index] = updated_education
            return jsonify(id=index, experience=updated_education), 200

        return jsonify({}), 404

    def handle_delete():
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['education']):
            deleted_education = data['education'].pop(index)
            return jsonify(deleted_education), 200

        return jsonify({}), 404

    methods = {
        'GET': handle_get,
        'POST': handle_post,
        'PUT': handle_put,
        'DELETE': handle_delete
    }
    handler = methods.get(request.method)
    if handler:
        return handler()

    return jsonify({}), 405

@app.route('/resume/skill', methods=['GET', 'POST', 'PUT', 'DELETE'])
def skill():
    '''
    Handles Skill requests
    '''

    def handle_get():
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
            return jsonify(data['skill'][index])
        return jsonify(data['skill'])

    def handle_post():
        request_data = request.get_json()
        required_fields = ["name", "proficiency", "logo"]
        is_valid, error_mssg = validate_fields(required_fields, request_data)

        if not is_valid:
            return jsonify({"error": error_mssg}), 400
        try:
            new_skill = Skill(**request_data)
            data["skill"].append(new_skill)
            return jsonify(skill=new_skill, id=len(data['skill'])-1), 201
        except TypeError as e:
            return jsonify({"error": str(e)}), 400

    def handle_put():
        request_data = request.get_json()
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
            updated_skill = Education(**request_data)
            data['skill'][index] = updated_skill
            return jsonify(id=index, experience=updated_skill), 200
        return jsonify({}), 404

    def handle_delete():
        index = request.args.get('index', type=int)
        if index is not None and 0 <= index < len(data['skill']):
            deleted_skill = data['skill'].pop(index)
            return jsonify(deleted_skill), 200
        return jsonify({}), 404

    methods = {
        'GET': handle_get,
        'POST': handle_post,
        'PUT': handle_put,
        'DELETE': handle_delete
    }
    handler = methods.get(request.method)
    if handler:
        return handler()

    return jsonify({}), 405
