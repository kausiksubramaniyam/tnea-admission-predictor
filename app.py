from flask import Flask,render_template,request,redirect,url_for
from main import predict_cutoff
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
   return render_template("mini.html")

@app.route('/choose',methods=['POST','GET'])
def college():
   return render_template("college.html")

@app.route('/predicts',methods = ['POST','GET'])
def predicts_cutoff():
   college = request.form['college']
   course = request.form['course']
   community = request.form['community']
   a=[college,course,community]
   try:
      cutoff=predict_cutoff(a)
      return render_template("cutoff.html",cutoff=cutoff[0]-2)
   except ModuleNotFoundError:
      return "Unable to find module."

if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)
