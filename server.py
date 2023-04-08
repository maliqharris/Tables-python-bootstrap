from flask import Flask, render_template  # Import Flask to allow us to create our app          render template to import out htmls!
from players import users 
# from players file import users list 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    print(users)
    return render_template('index.html', players_for_jinjia = users) 
  # Return the string version of file name  return var players(can be anything) = users(my list!)










if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

