from flask import Flask
from privateGPT2 import main as privateGPT2_main  # Importing the main function from privateGPT2.py

# Create a Flask app instance with the name "myapp"
myapp = Flask(__name__)

# Define a route for the root URL
@myapp.route('/')
def hello():
    # Call the main function from privateGPT2.py
    result = privateGPT2_main()
    return f'Hello, World! Result from privateGPT2: {result}'

# Run the app if this script is executed
if __name__ == '__main__':
    myapp.run(debug=True)
