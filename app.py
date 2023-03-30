from flask import Flask, render_template, request, url_for, redirect
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def user():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Boutique"))

        result_dicts = []

        for row in result.all():
            result_dicts.append(row._asdict())
        
        return result_dicts
    
@app.route('/')
def hello():
    result = user()
    return render_template('home.html', result = result)


# @app.route("/")
# def home():
#     return render_template('home.html' )

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user_name = request.form['name']
#         user_shop = request.form['shop']
#         return redirect(url_for("home", usr = user_name, shp = user_shop))
#     else:
#         return render_template('form.html')
    

    
# @app.route('/live/<usr>')
# def user(usr, shp):
#     return f'le nom du propriétaire est {usr} et sa boutique c\'est {shp}'

# @app.route('/')
# def hello_world():
#     f = open("output.json", 'r')
#     out = f.read()
#     out = json.loads(out)
#     return render_template("form.html", out=out, id=2)
#     # if output['id'=1]:
#     #     print(output['title'])
#     # return
    
# @app.route('/liveCreate/', methods=['GET'])
# def liveCreate():
#     form = request.args['name']
#     return f'traitement des données {form}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)