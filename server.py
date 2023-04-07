from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "it works!"
    

@app.route("/table")
def fill_table():
  users = (
   {'full_name': 'Michael Choi','first_name' : 'Michael', 'last_name' : 'Choi', 'entry_number': '1'},
   {'full_name': 'John Supsupin','first_name' : 'John', 'last_name' : 'Supsupin', 'entry_number': '2'},
   {'full_name': 'Mark Guillen','first_name' : 'Mark', 'last_name' : 'Guillen', 'entry_number': '3'},
   {'full_name': 'KB Tonel','first_name' : 'KB', 'last_name' : 'Tonel', 'entry_number': '4'}
  )

  return render_template("index.html", users = users)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.