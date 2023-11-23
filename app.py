from flask import Flask,render_template,url_for


app = Flask(__name__)


@app.route('/Tours')
def Tours():
    return render_template('Tours.html')

@app.route('/Kerala')
def Kerala():
    return render_template('Kerala.html')

@app.route('/fi')
def fi():
    return render_template('finical.html')

@app.route('/Goa')
def Goa():
    return render_template('Goa.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Ladakh')
def Ladakh():
    return render_template('Ladakh.html')    

@app.route('/ourpartners')
def ourpartners():
    return render_template('ourpartners.html')

@app.route('/Lambasingi')
def Lambasingi():
    return render_template('Lambasingi.html')

@app.route('/Maharastra')
def Maharastra():
    return render_template('Maharastra.html')

@app.route('/Tamilnadu')
def Tamilnadu():
    return render_template('Tamilnadu.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/Araku')
def Araku():
    return render_template('Araku.html')

@app.route('/Varanasi')
def Varanasi():
    return render_template('Varanasi.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup/login')
def signup():
    return render_template('signup.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__=='__main__':
    app.run(debug=True)