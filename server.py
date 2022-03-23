from  flask import Flask , render_template  
app = Flask(__name__)

@app.route('/')                           
def Checker_Board():
   
    return render_template('checkerboard.html')  

@app.route('/Hi')
def display():

    return render_template('check.html', times=4)
    
if __name__=="__main__":
    app.run(debug=True)                  