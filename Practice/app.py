from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Kivy app running!"

def run_kivy():
    subprocess.Popen(["python", "main.py"])

if __name__ == '__main__':
    run_kivy()  # Start the Kivy app when the Flask server starts
    app.run(debug=True, use_reloader=False)  # Disable Flask's built-in reloader
