from flask import Flask
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

app = Flask(__name__)

# Access environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def home():
    return f"Secret Key: {app.config['SECRET_KEY']}"

if __name__ == '__main__':
    app.run(debug=True)