# Query student data from schoolharbor graphql via flask app
from schoolharbor_flask_graphQL import fetch_data_from_graphql

def get_student_data():
    query = '''
    {
        students {
            studentId {value}
            dateOfBirth
        }
    }
    '''
    return fetch_data_from_graphql(query)
