# **Take-Home Assignment Part 2: "Basic API Testing"**

## **Context**
Write simple automated tests for a REST API to demonstrate basic QA automation skills relevant to testing cloud-based platforms.

## **Requirements**
**Language:** Use the same language from Part 1 (JavaScript, Python, C#, or Go)  
**Target API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - a free REST API for testing

## **Tasks** (20-25 minutes)
Write **3 automated test cases** that cover:

1. **GET request** - Fetch a user and validate response structure
   - Test endpoint: `GET /users/1`
   - Validate: 200 status code, required fields exist (id, name, email)

2. **POST request** - Create a new post and verify creation  
   - Test endpoint: `POST /posts`
   - Send JSON data and validate the response

3. **Error handling** - Test 404 response for non-existent resource
   - Test endpoint: `GET /users/999` 
   - Validate: 404 status code and appropriate response

## **Test Framework**
Use any common testing framework for your chosen language:
- **JavaScript:** Jest, Mocha, or similar
- **Python:** pytest, unittest, or similar  
- **C#:** xUnit, NUnit, or similar
- **Go:** testing package or similar

## **Example Structure**

```javascript
// JavaScript example
describe('JSONPlaceholder API Tests', () => {
  test('should fetch user successfully', async () => {
    // Your implementation here
  });

  test('should create new post', async () => {
    // Your implementation here  
  });

  test('should handle non-existent user', async () => {
    // Your implementation here
  });
});
```

```python
# Python example
class TestJSONPlaceholderAPI:
    def test_fetch_user_successfully(self):
        # Your implementation here
        
    def test_create_new_post(self):
        # Your implementation here
        
    def test_handle_nonexistent_user(self):
        # Your implementation here
```

## **Documentation** (5 minutes)
- **Brief comments** in your test code explaining what each test validates
- **Simple run instructions** - how to install dependencies and run tests

## **Deliverables**
- Working test code that covers the 3 scenarios
- Basic run instructions (can be comments in the file or separate README)

## **Evaluation Focus**
- **API Testing Knowledge:** Understanding of GET/POST requests and HTTP status codes
- **Test Structure:** Clear test organization and meaningful test names
- **Assertions:** Proper validation of responses and data
- **QA Thinking:** Appropriate test scenarios and edge case consideration

**Time Estimate:** 30 minutes

## **Notes**
# - Focus on demonstrating QA automation fundamentals
# - Simple, working tests are better than complex, broken ones
# - You can use any HTTP client library (fetch, requests, HttpClient, etc.)

# Basic API Testing using Python 

%pip install requests pytest # Make HTTP requests to the API endpoints.
import requests

base_url = "https://jsonplaceholder.typicode.com/"
endpoints_to_test = {
  "get_all_post": {"path": "/posts", "method": "GET"},
  "get_single_post": {"path": "/posts/1", "method": "GET"},
  "get_comments_for_post": {"path": "/posts/1/comments", "method": "GET"},
}
# The code above defines the base URL for the API being tested, and a list of some initial endpoints with their HTTP methods.

#Below we have three functions for the specific test cases requested
# The first test makes a GET request to the /posts endpoints of the JSONPlaceholder API, which returns a list of all posts.
def test_get_all_posts(self):
  response = requests.get(f"{base_url}{endpoints_to_test['get_all_posts']['path']}")
  assert response.status_code == 200 # Checks the HTTP status code of the response is 200, validating the request was successful.
  assert isinstance(response.json(), list) # Checks the body of the response, which validates the API is returning a collection of items.
# This next test makes a GET request to the /posts/1 endpoint to return a single post with the ID of 1.  
def test_get_single_post():
  response = requests.get(f"{base_url}{endpoints_to_test['get_single_post']['path']}")
  assert response.status_code == 200
  assert isinstance(response.json(), dict) # Checks the response body is a Python dictionary, validating the API is returning a single post.
# This next test makes a GET request to the /posts/1/comments endpoint, which should return comments associated with the post that has ID 1.
def test_get_comments_for_posts():
  response = requests.get(f"{base_url}{endpoints_to_test['get_comments_for_post']['path']}")
  assert response.status_code == 200
  assert isinstance(response.json(), list) # Checks the response body is a Python list, as an endpoint providing comments for a post.

# Test class with integrated test cases
# This next test makes a GET request to the /users/1 endpoint to fetch a specific user by ID.
class TestJSONPlaceholderAPI:
  def test_fetch_user_successfully():
    """Test case for fetching a user and validating response structure."""
user_id = 1
response = requests.get(f"{base_url}/users/{user_id}")
assert response.status_code == 200 # Validates successful retrieval of the user ID
user_data = response.json()
assert isinstance(user_data, dict) # Checks the response body is a Python dictionary, representing a single user. 
assert "id" in user_data # Verifies the returned user dictionary contains an "id" field.
assert "name" in user_data # Verifies the returned user dictionary contains a "name" field.
assert "email" in user_data # Verifies the returned user dictionary contains an "email" field.
# Assert statements check the response's status code and data structure.
# This next test sends a POST request to the /posts endpoint.
def test_create_new_post(self):
  """Test case for creating a new post and verifying creation."""
  new_post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
    }
  response = requests.post(f"{base_url}/posts", json=new_post_data)
  assert response.status_code == 201 # Checks that the status of the code is 201, which is the standard for a successful resource creation via POST.
  created_post = response.json()
  assert isinstance(created_post, dict) # Checks response body is a dictionary containing details of newly created resource. 
  assert "id" in created_post # Checks response has an "id" for the newly created post.
  assert created_post["title"] == new_post_data["title"] # Verifies the "title" in the response matches the title sent in the request. 
  assert created_post["body"] == new_post_data["body"] # Verifies the "body" in the response matched the body sent in the request. 
  assert created_post["userId"] == new_post_data["userId"] # Verifies the "userId" in the response matches the userId sent in the request. 
# This test makes a GET request to the /users/999 endpoint using an ID that is expected to correspond to a non-existent user.
def test_handle_nonexistent_user(self):
  """Test case for testing 404 response for non-existent resource."""
  user_id = 999
  response = requests.get(f"{base_url}/users/{user_id}")
  assert response.status_code == 404 # Checks the status of the code is 404. 

!pytest  # Attempts to run the tests.

# Also can manually execute each test function to simulate running the tests as seen below.
test_get_all_posts()
test_get_single_post()
test_get_comments_for_posts()
test_fetch_user_successfully()
test_create_new_post()
test_handle_nonexistent_user()
print("Tests executed.")
