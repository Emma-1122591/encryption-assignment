from flask import Flask, render_template, jsonify, request
from cryptography.fernet import Fernet
from utils.key_loader import load_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        key = load_key()
        fernet = Fernet(key)
        encrypted_text = fernet.encrypt(text.encode())
        return render_template('index.html', encrypted_text=encrypted_text)          
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)