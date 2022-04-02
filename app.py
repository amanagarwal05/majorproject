#from crypt import methods
#from multiprocessing import connection
from random import sample
from select import select
from ssl import ALERT_DESCRIPTION_USER_CANCELLED
from tkinter import EXCEPTION, Y
from tkinter.font import NORMAL
from RNF_CLF import clf_6
#from XGBOOST_CLF import xgb_clf_15
from flask import Flask, render_template , request
import pandas as pd
import mysql.connector

#data=None
headings=("feature_1","feature_2","feature_3","feature_4","feature_5","feature_6","attack_type")
app=Flask(__name__)
mysql_db=mysql.connector.connect(host="localhost",user="root",password="Shyambaba@20",database="rnf")
mycursor=mysql_db.cursor()
attack_types={
    0:"DOS",
    1:"NORMAL",
    2:"PROBE",
    3:"R2L",
    4:"U2R"
}

checkbox_titles={
    "no_attack":"NORMAL",
    "r2l":"R2L",
    "probe":"PROBE",
    "dos":"DOS",
    "u2r":"U2R"
}

@app.route('/Home')
def home():
    return render_template('IDS_Main.html')

@app.route('/Home/networktraffic')
def table():
    select_stmnt="""select * from ids"""
    mycursor.execute(select_stmnt)
    data=mycursor.fetchall()
    headings=("feature_1","feature_2","feature_3","feature_4","feature_5","feature_6","attack_type")
    return render_template('page_2.html',headings=headings,data=data)

@app.route('/Home/networktraffic/datafilter',methods=['GET','POST'])
def filter_data(): 
    #for attack_type in ["no_attack","u2r","probe","dos","r2l"]:
    if request.method=="POST":
        value=request.form.get("checkbox")
        print(value)
            #if value:
        attack_name=checkbox_titles.get(value)
            #query=("select * from ids where attack_type=%s")
            #params=(attack_name)
            #mycursor.execute(query,params)
        query = "SELECT * FROM ids WHERE attack_type = %(attack_name)s"
        mycursor.execute(query, { 'attack_name': attack_name })
        data=mycursor.fetchall()
        return render_template('page_2.html',headings=headings,data=data)
    else:
        return render_template('page_2.html')
        #headings=("feature_1","feature_2","feature_3","feature_4","feature_5","feature_6","attack_type")
    #return render_template('page_2.html',headings=headings,data=data)
    
    

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
    print(type(prediction))
    #prediction=xgb_clf_15.predict(testcase)
    try:
        #mysql_db=mysql.connector.connect(host="localhost",user="root",password="Shyambaba@20",database="rnf")
        #mycursor=mysql_db.cursor()
        attack_name=attack_types.get(prediction[0])
        sql_stmnt="""INSERT INTO ids(feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,attack_type) VALUES(%s,%s,%s,%s,%s,%s,%s)"""

    
        data=(t1,t2,t3,t4,t5,t6,attack_name)
    
        mycursor.execute(sql_stmnt,data)
        mysql_db.commit()
        print("aman")
    except Exception as e:
        mysql_db.rollback()
        print(e)
    return render_template('print.html',v1=t1,v2=t2,v3=t3,v4=t4,v5=t5,v6=t6,pred=prediction)



if __name__ == '__main__':
    app.run(debug=True)