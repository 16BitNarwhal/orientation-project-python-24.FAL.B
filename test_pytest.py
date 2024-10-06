'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Add a new education and then get all educations. 
    
    Check that it returns the new education in that list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/education')
    assert response.json[item_id] == example_education


def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill

def test_edit_education():
    '''
    Add a new education, then edit it and get the updated experience. 
    
    Check that the updated education is returned
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }

    post_response = app.test_client().post('/resume/eudcation',
                                     json=example_education)
    item_id = post_response.json['id']

    updated_education = {
        "course": "Computer Science",
        "school": "NYU",
        "start_date": "October 2024",
        "end_date": "August 2026",
        "grade": "98%",
        "logo": "example-logo.png"
    }

    response = app.test_client().put('/resume/education',
                                     json={"experience": updated_education, "id": item_id})
    assert response.json['experience'] == updated_education
    assert response.json['id'] == item_id
    assert response.status_code == 200


def test_edit_skill():
    '''
    Add a new skill, then edit it and get the updated experience. 
    
    Check that the updated skill is returned
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    post_response = app.test_client().post('/resume/skill',
                                     json=example_skill)
    item_id = post_response.json['id']

    updated_skill = {
        "name": "TypeScript",
        "proficiency": "1-4 years",
        "logo": "example-logo.png"
    }

    response = app.test_client().put('/resume/skill',
                                     json={"experience": updated_skill, "id": item_id})
    assert response.json['experience'] == updated_skill
    assert response.json['id'] == item_id
    assert response.status_code == 200
    
def test_skills_delete_index():
    """
    Test the successful deletion of skills entries at index.
    """
    example_skills = [
    {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    },
    {
        "name": "TypeScript",
        "proficiency": "1-3 years",
        "logo": "example-logo.png"
    }]

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skills).json['id']

    response = app.test_client().delete(f'/resume/skill?index={item_id}')
    assert response.status_code == 200
    assert response.json[item_id] == example_skills[item_id]

    response_items = app.test_client().get('/resume/skill')
    assert response_items.json is None

def test_education_delete_index():
    """
    Test the successful deletion of education entries at index.
    """
    example_education = [
    {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    },
    {
        "course": "Computer Science",
        "school": "UT",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "97%",
        "logo": "example-logo.png"
    }]

    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().delete(f'/resume/education?index={item_id}')
    assert response.status_code == 200
    assert response.json[item_id] == example_education[item_id]

    response_items = app.test_client().get('/resume/education')
    assert response_items.json is None
    