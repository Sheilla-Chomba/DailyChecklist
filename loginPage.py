from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Templates', static_folder='Static')


@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')

        if email == 'trial@kra.go.ke' and password == '1234567890':
            return render_template('homepage.html')
        else:
            error = 'Invalid email or password'
            return render_template('loginpage.html', error=error)

    return render_template('loginpage.html')


if __name__ == '__main__':
    app.run(debug=True)  # Allows the program to be debugged as it runs
