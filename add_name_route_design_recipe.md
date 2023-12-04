# {{ NAME }} Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Names route
GET /names?name=<string>

params:
    name: string

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# GET /names?name=Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /names
  Expected response (200 OK):
  Julia, Alice, Karim, Eddie
"""
def test_get_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
GET /names
  Expected response (200 OK):
  Julia, Alice, Karim, Sabirah
"""
def test_get_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Sabirah'