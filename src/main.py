# main.py
"# Main Entry Point

# Import Required Modules including Flask
from Flask import Flask, request, *son
from image_to_text_libs import text_from_image
from config import get_config

app = Flask(__name__)

@app.route('/submit-task')
def submit_task():
    data = request.get(json)
    # Add task processing here
    return json( {"status": "success"})

@app.route('/get-result')
def get_result():
    result = "Some processed result..."
    return json({'data': result})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)