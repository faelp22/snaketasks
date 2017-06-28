"""
The main
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    """
    Main
    """
    return "Hello World!"

