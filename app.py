from flask import Flask,request,render_template, redirect, url_for, session
from controllers import IndexController as main
#Flask initialization
app = Flask(__name__)
app.secret_key = "ecommerce"
app.config['SECRET_KEY'] = "ecommerce"

@app.route("/index")
def index():
    success,resp = main.index()
    if success != 1:
        return redirect(url_for('error_page', message=resp))
    else:
        username = session['username'] 
        return render_template("index.html", resp=resp,username=username)
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route('/login-form', methods=['POST'])
def login_form():
    username = request.form['username']
    password = request.form['password']
    # Do something with the username and password, like saving to a database
    print(f"Username: {username}, Password: {password}")
    success,resp = main.Login(username,password)
    print(resp)
    if success != 1:
        return render_template('error_page.html', message=resp)
    else:
        session['username'] = resp
        return render_template("welcome.html", username=resp)
    
@app.route('/signup-form', methods=['POST'])
def signup_form():
    username = request.form['username']
    password = request.form['password']
    # Do something with the username and password, like saving to a database
    print(f"Username: {username}, Password: {password}")
    success,resp = main.Signup(username,password)
    print(resp)
    if success != 1:
        return render_template('error_page.html', message=resp)
    else:
        session['username'] = username
        return render_template("welcome.html", username=username)


@app.route('/category/<category>')
def category(category):
    success,resp = main.category(category=category)
    if success != 1:
        # return redirect(url_for('error', message=resp))
        return render_template('error.html', message=resp)

    else:
        return render_template("category.html", resp=resp,category=category)

@app.route("/jewellery")
def jewellery():
    return render_template("jewellery.html")

@app.route("/fashion")
def fashion():
    return render_template("fashion.html")

@app.route("/electronic")
def electronic():
    return render_template("electronic.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)
    # app.run()