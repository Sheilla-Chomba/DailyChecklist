from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('loginpage.html')

if __name__ == '__main__':
    app.run()

# gradient was at 0.4 both