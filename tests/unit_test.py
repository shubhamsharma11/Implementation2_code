from ..code import app
from flask.testing import FlaskClient

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Case Passed !!' in response.data