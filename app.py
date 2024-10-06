import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    name = os.getenv('NAME')
    age = os.getenv('AGE')
    location = os.getenv('LOCATION')
    skills = os.getenv('SKILLS')
    schooling = os.getenv('SCHOOLING')
    graduation = os.getenv('GRADUATION')
    course = os.getenv('COURSE')
    description = os.getenv('DESCRIPTION')
    return render_template(
        'index.html',
        name=name, 
        age=age, 
        location=location, 
        skills=skills, 
        schooling=schooling, 
        graduation=graduation, 
        course=course, 
        description=description
        )


if __name__ == "__main__":
    app.run(debug=True)