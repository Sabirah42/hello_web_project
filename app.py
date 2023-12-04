import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # The value is 'Leo'
    message = request.form['message'] # The value is 'Hello world"

    # Send back a confirmation of name and message
    return f"Thanks, {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    num_vowels = 0

    for letter in text:
        if letter in 'aeiou':
            num_vowels += 1

    return f'There are {num_vowels} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    sorted_names = ','.join(sorted(names.split(",")))
    return sorted_names

@app.route('/names', methods=['GET'])
def names():
    name = request.args['name']
    names = f'Julia, Alice, Karim, {name}'
    sorted_names = ', '.join(sorted(names.split(", ")))

    return sorted_names

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

