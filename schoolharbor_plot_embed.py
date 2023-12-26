# Import packages
import pandas as pd
import plotly.express
import requests
import plotly.express as px

# Incorporate data & connect to API
url = 'https://schoolharborgraphql-test.azurewebsites.net/GraphQL/'
bearer_token = 'ilde01'

# Function to check the status of the bearer token
def check_token_status(url, bearer_token):
    try:
        response = requests.post(url, headers={'Authorization': f'Bearer {bearer_token}'})
        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error while checking token status: {e}")
        return False  # Assume token is invalid in case of any exception

# Initialize an empty DataFrame with necessary columns
df = pd.DataFrame(columns=['studentId', 'dateOfBirth'])

token_status = check_token_status(url, bearer_token)

# If the token is valid, proceed with the API query
if token_status:
    graphql_query = '''
    {
        students {
            studentId {value}
            dateOfBirth
        }
    }
    '''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer_token}',
    }
    payload = {
        'query': graphql_query,
    }
    response = requests.post(url, headers=headers, json=payload)
    json_response = response.json()
    students_data = json_response.get('data', {}).get('students', [])
    df = pd.DataFrame(students_data)

# If the token is invalid, use the alternative data source for students_data
else:
    students_data = pd.read_excel('AltSource.xlsx', sheet_name='fake_students')
    df = pd.DataFrame(students_data)

df['year_month'] = df['dateOfBirth'].str[:7]
df = df.groupby('year_month').size().reset_index(name='Student_Count')

#plot
fig = plotly.express.bar(df, x='year_month', y='Student_Count')
print(token_status)
fig.show()
#fig.write_html('students.html')