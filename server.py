from flask import Flask, redirect, render_template
app = Flask(__name__)    

@app.route('/')          
def index(methods='POST'):
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    return render_template('index.html')  
@app.route('/whatever')
    

if __name__=="__main__":     
    app.run(debug=True)   
