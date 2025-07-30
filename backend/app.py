import os
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if name and email and message:
        return jsonify({'message': 'Message received'})
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)
