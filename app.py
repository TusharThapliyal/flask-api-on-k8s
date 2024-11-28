from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/save">
            <label for="message">Enter your message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
            <button type="submit">Save Message</button>
        </form>
    '''

@app.route('/save', methods=['POST'])
def save_message():
    message = request.form.get('message')  # Get the input from the form
    if message:
        with open('/home/tushar/app/app-data/message.txt', 'w') as f:
            f.write(message)  # Save the input to message.txt
        return "Message saved successfully!"
    else:
        return "No message provided. Please enter a message."


@app.route("/message")
def home():
    # Reading configuration from environment variables
    app_name = os.getenv("APP_NAME", "Default App Name")
    app_env = os.getenv("APP_ENV", "Default Environment")

    # Reading secret values from environment variables
    db_username = os.getenv("DB_USERNAME", "No Username Set")
    db_password = os.getenv("DB_PASSWORD", "No Password Set")

    # Reading file content from mounted volume
    try:
        with open("/home/tushar/app/app-data/message.txt", "r") as file:
            message = file.read()
    except FileNotFoundError:
        message = "No message found."

    return f"""
    <h1>{app_name}</h1>
    <p>Environment: {app_env}</p>
    <p>Database Username: {db_username}</p>
    <p>Database Password: {db_password}</p>
    <p>Message: {message}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

