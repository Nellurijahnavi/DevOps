from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
    
        return render_template('succes.html')
    return render_template('reg.html')
if __name__ == '__main__':
   app.run(debug=True)
