# Use students query, transform result for expected plotly.js use case
from flask import render_template
from schoolharbor_flask_graphQL import app
from student_data import get_student_data

@app.route('/')
def index():
    result = get_student_data()

    if result:
        data = result.get('data', {}).get('students', {})

        perform_analytics(data)  # Placeholder for any transformations or calculations needed before returning template

        return render_template('index.html', data=data)
    else:
        return "Failed to fetch data from the GraphQL API."


if __name__ == '__main__':
    app.run(debug=True)
