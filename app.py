from flask import Flask, render_template # Imports necessary for Flask

app = Flask(__name__) # Initialize app variable 

@app.route('/') # Route for default login page on app
def index():
    return render_template("login_page.html")



if (__name__ == '__main__'): # Launch app in local host when file is run
    app.run(debug=True)



