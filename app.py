from flask import Flask, render_template
import signal
import sys

app = Flask(__name__)

@app.route('/')
def app_func():
    return render_template('app.html')

def graceful_exit(signum, frame):
    print("\nShutting down the Flask app gracefully...")
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, graceful_exit)
signal.signal(signal.SIGTERM, graceful_exit)

if __name__ == '__main__':
    print("Starting Flask app. Press Ctrl+C to stop.")
    app.run(debug=True)

