# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Returns a simple greeting."""
    # Example of using an environment variable
    greeting = os.environ.get("GREETING", "Hello")
    return f"{greeting}, Dockerized World!"

# Example route for health check
@app.route('/health')
def health_check():
    """Simple health check endpoint."""
    return "OK", 200

if __name__ == "__main__":
    # Run on port 5000, accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
