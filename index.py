from flask import Flask, render_template, request, redirect, url_for
from model import probe_model_5l_profit
import json
app = Flask(__name__, template_folder='app/templates')


@app.route('/')
def index():
    return render_template('page1.html')


@app.route('/process_data', methods=['POST'])
def process_data():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    # Read the content of the uploaded file
    content = file.read().decode('utf-8')

    # Convert to JSON
    data = json.loads(content)

    # Assuming you have a function to process the data
    results = probe_model_5l_profit(data["data"])

    return render_template('page2.html', results=results)
if __name__ == '__main__':
    app.run(debug=True)
