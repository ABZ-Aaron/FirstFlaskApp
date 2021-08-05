from flask import Flask, render_template, url_for
from forms import LoginForm, RegistrationForm

# Create instance of flask application
app = Flask(__name__) 

app.config['SECRET_KEY'] = '9b51f8b65b7a2455cd890f97d1fd03c3'

# We can pass these dictionaries into our templates by adding them
# as an argument to render_template.
posts = [
    {
        'author' : "Corey Shafer",
        'title' : 'blog',
        'content' : "first post content",
        "date_posted" : 'April 20, 1991'
    },
    {
        'author' : "Aaron Wright",
        'title' : 'blog 1',
        'content' : "second post content",
        "date_posted" : 'May 21, 2000'
    }
]

# This @ will handle all of the complicated backend stuff. The '/' is just our route 
# page of our website e.g. homepage. 
@app.route("/") 
@app.route("/home") 
def home():
    # We are using the render_template function to read a HTML file
    return render_template("home.html", posts = posts)

# This creates a new route - about page
@app.route("/about") 
def about():
    return render_template("about.html", title = "About")

@app.route("/register") 
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login") 
def login():
    form = RegistrationForm()
    return render_template('login.html', title = 'Login', form = form)

# This will run our app
if __name__ == "__main__":
    app.run(debug = True)

txt = 'I love apples, apple are my favorite fruit'

x = txt.count('apple', 10, 24)

print(x)
