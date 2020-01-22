from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def student():
   return render_template('formindex.html')

@app.route('/predict',methods = ['POST','GET' ])
def predict():
    f=[]
    result=request.form
    int_fe=[x for x in request.form.values()]
    c=0
    for i in int_fe:
        if c<3:
            continue
        else:

            f.append(i)

    dtest12=pd.DataFrame({'q1':3,'q2':4,'q3':5,'q4':5,'q5':3,'q6':2,'q7':1,'q8':5,'q9':2,'q10':3,'q11':3,'q12':2,'q13':4,'q14':3,'q15':5,'q16':3,'q17':3,'q18':1,'q19':3,'q20':2},index=[0])
    print("dictionary is : ",dtest12)
    #final_features=[np.array(int_features)]
    prediction=model.predict(dtest12)
    output=prediction[0]
    print("prediction is : ",output)
    print("requested data is : ",result)
    return render_template('formindex.html',prediction_text="career recommended is $ {}".format(output))




if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port="1173")


