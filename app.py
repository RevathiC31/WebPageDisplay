
"""
app.py

A simple Flask web application that serves a homepage and handles graceful shutdown
on receiving termination signals (SIGINT or SIGTERM).

Author: Revathi C
Date: 18-06-2025
"""
from flask import Flask, render_template
import signal
import sys

app = Flask(__name__)

@app.route('/')
def app_func():
    
    """
    Route for the homepage.

    Returns:
        Rendered HTML template for the home page.
    """

    return render_template('app.html')

def graceful_exit(signum, frame):
    
    """
    Handles graceful shutdown of the Flask app when a termination signal is received.

    Args:
        signum (int): The signal number.
        frame (frame object): Current stack frame (not used).
    """

    print("\nShutting down the Flask app gracefully...")
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, graceful_exit)
signal.signal(signal.SIGTERM, graceful_exit)

if __name__ == '__main__':
    
    """
    Entry point of the application. Starts the Flask development server.
    """
    print("Starting Flask app. Press Ctrl+C to stop.")
    app.run(debug=True)

