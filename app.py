from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from utils.key_loader import load_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("text-encryption"):
            text = request.form.get("text-encryption")
            key = load_key()
            fernet = Fernet(key)
            encrypted_text = fernet.encrypt(text.encode())
            return render_template('index.html', encrypted_text=encrypted_text)
        elif request.form.get("text-decryption"):
            text = request.form.get("text-decryption")
            key = load_key()
            fernet = Fernet(key)
            decrypted_text = fernet.decrypt(text.encode()).decode()
            return render_template('index.html', decrypted_text=decrypted_text)          
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)