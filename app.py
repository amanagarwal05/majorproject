from tkinter import EXCEPTION
from RNF_CLF import clf_6
from flask import Flask, render_template , request
import pandas as pd
import mysql.connector

app=Flask(__name__)

@app.route('/Home')
def home():
    return render_template('IDS_Main.html')

@app.route('/',methods=['POST'])
def getvalue():

    t1=request.form['t1']
    t2=request.form['t2']
    t3=request.form['t3']
    t4=request.form['t4']
    t5=request.form['t5']
    t6=request.form['t6']

    testcase=pd.DataFrame([[t1,t2,t3,t4,t5,t6]])
    
    prediction=clf_6.predict(testcase)
    mysql_db=mysql.connector.connect(host="localhost",user="root",password="Shyambaba@20",database="rnf")
    mycursor=mysql_db.cursor()
    sql_stmnt="INSERT INTO ids(feauture_1,feauture_2,feauture_3,feauture_4,feauture_5,feauture_6) VALUES(%d,%d,%d,%d,%d,%d)"
    data=(t1,t2,t3,t4,t5,t6)
    try:
        mycursor.execute(sql_stmnt,data)
    except EXCEPTION as e:
        mysql_db.rollback()
        print(e)
    return render_template('print.html',v1=t1,v2=t2,v3=t3,v4=t4,v5=t5,v6=t6,pred=prediction)



if __name__ == '__main__':
    app.run(debug=True)
