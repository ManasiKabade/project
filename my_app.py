from flask import Flask,render_template,request
app=Flask(__name__,template_folder="template")

@app.route("/")
def home():
  return render_template("demo.html")

@app.route("/demo.html")
def getprediction(enginHP):
  import pickle
  import os
  p = os.path.dirname(__file__)
  filepath = os.path.join(p,'model.data')
  model = pickle.load(open(filepath,'rb'))
  y_predict=model.predict([[enginHP]])
  return y_predict[0] 

@app.route('/calc',methods=['get','post'])
def calc():
    enginHP = request.form['EnginHP']
    p=getprediction(int(enginHP))    
    return  "Answer" + str(p)


if __name__=="__main__":
    app.run(debug=True)


