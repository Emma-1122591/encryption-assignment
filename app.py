from flask import Flask, render_template, jsonify, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        if text:
            pass
        return render_template('index.html', encrypted_text=text)          
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)