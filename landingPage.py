from flask import Flask, render_template, request
from loginPage import login

app = Flask(__name__, template_folder='Templates', static_folder='Static')


@app.route("/", methods=['POST', 'GET'])
def landingPage():
    if request.method == 'POST' :
        return login()                      #render_template('loginpage.html') just trial, not to be deleted
    return render_template('landingPage.html')



if __name__ == '__main__':
    app.run(debug=True)  # Allows the program to be debugged as it runs

