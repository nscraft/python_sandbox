from flask import Flask
import requests

app = Flask(__name__)

GRAPHQL_API_ENDPOINT = 'https://schoolharborgraphql-test.azurewebsites.net/GraphQL/'
bearer_token = 'ilde01'  # Update with real token


def fetch_data_from_graphql(query):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer_token}'
    }
    data = {'query': query}
    response = requests.post(GRAPHQL_API_ENDPOINT, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)
