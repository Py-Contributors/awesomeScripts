from flask import *
from bs4 import BeautifulSoup
import requests
import time
from flask_sqlalchemy import *
import json
import re
import mysql.connector

import pandas as pd
import numpy as np
app=Flask(__name__)
app.config["DEBUG"]=True
app.secret_key="HELLO_MATE@1"
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:MYPASSWORD@localhost:3306/Scraped"
app.config["SQLALCHEMY_ECHO"] = True

db=SQLAlchemy(app)
app.secret_key="Aezakmirocketman@1"
class Big(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	Product=db.Column(db.String(1156),unique=False,nullable=False)
	Ratings=db.Column(db.String(1150),unique=False,nullable=False)
	Price=db.Column(db.Integer,unique=False ,nullable=False)


@app.route("/",methods=["GET","POST"])

def home():
	if request.method=="POST":
		g=request.form["txt"]
		if g=="Fashion" or "fashion":
			return redirect(url_for("linkerfashion"))
		else:
			return redirect(url_for("linkertech"))


	return render_template("register.html")

@app.route("/link/Fashion",methods=["GET","POST"])
def linkerfashion():
	op=[]
	src={}
	products=[]
	ratings=[]
	price=[]
	description=[]
	image_link=[]
	pages=[]
	New=""
	
	error=None
	c=0
	if request.method=="POST":
		e=request.form
		LINK=e["linked"]
		data=requests.get(LINK)
		print(data.status_code)
		#print(request.params)
		if data.status_code!=200:
			return "ERROR"
		else:
			data=data.content
			soup=BeautifulSoup(data,"html.parser")
			for d in soup.find_all("div",class_="_2LFGJH"):
				products.append(d.find("a",class_="_2mylT6").get("title"))
				#try:
					#ratings.append(float(d.find("div",class_="hGSR34").get_text()))
				#except:
				ratings.append(float(0))
				if d.find("div",class_="_1vC4OE") !=None:
					price.append(d.find("div",class_="_1vC4OE").get_text())
				else:
					price.append(0)
				#if d.find("div",class_="_1vC4OE") !=None:
					#description.append(d.find("div",class_="_1rcHFq").get_text())
				#else:
					#description.append("SOORY! NO description")




			for i in soup.find_all("a",class_="_2Xp0TH"):
				pages.append(int(i.get_text()))
			for j in range(2,max(pages)+1):
				New=LINK+f"&pages{str(i)}"
				f=requests.get(New)
				f=f.content
				s=BeautifulSoup(f,"html.parser")
				for k in s.find_all("div",class_="_2LFGJH"):
					products.append(k.find("a",class_="_2mylT6").get("title"))
					#if k.find("div",class_="hGSR34")!=None:
						#ratings.append(float(k.find("div",class_="hGSR34").get_text()))
					#else:
					ratings.append(float(0))
					if k.find("div",class_="_1vC4OE") !=None:
						price.append(k.find("div",class_="_1vC4OE").get_text())
					else:
						price.append(0)
					#if k.find("div",class_="_1vC4OE") !=None:
						#description.append(k.find("div",class_="_1rcHFq").get_text())
					#else:
						#description.append("SOORY! NO description")



			for i in range(len(products)):
				price[i]=int(re.sub("[^0-9&.]","",price[i]))
				user=Big(Product=products[i],Ratings=ratings[i],Price=price[i])
				db.session.add(user)
				db.session.commit()
				
				src[str(i)]={"PRODUCTS":products[i],"PRICES":price[i],"RATINGS":ratings[i]}
			session["FASHION_PRODUCT"]=products
			session["FASHION_PRICE"]=price
			session["FASHION_RATINGS"]=ratings

			data=json.dumps(src,indent=5)
			#with open(".json","w") as file:
				#json.dump(data,file)


		return data
	return render_template("main_link.html")




@app.route("/link/Tech",methods=["GET","POST"])
def linkertech():
	op=[]
	src={}
	products=[]
	ratings=[]
	price=[]
	description=[]
	image_link=[]
	pages=[]
	New=""
	
	error=None
	c=0
	if request.method=="POST":
		e=request.form
		LINK=e["linked"]
		data=requests.get(LINK)
		print(data.status_code)
		#print(request.params)
		if data.status_code!=200:
			return "ERROR"
		else:
			data=data.content
			soup=BeautifulSoup(data,"html.parser")
			for d in soup.find_all("div",class_="_3liAhj"):
				products.append(d.find("a",class_="_2cLu-l").get("title"))

				ratings.append(float(0))
				if d.find("div",class_="_1vC4OE") !=None:
					price.append(d.find("div",class_="_1vC4OE").get_text())
				else:
					price.append(0)
				#if d.find("div",class_="_1vC4OE") !=None:
					#description.append(d.find("div",class_="_1rcHFq").get_text())
				#else:
					#description.append("SOORY! NO description")




			for i in soup.find_all("a",class_="_2Xp0TH"):
				pages.append(int(i.get_text()))
			for j in range(2,max(pages)+1):
				New=LINK+f"&pages{str(i)}"
				f=requests.get(New)
				f=f.content
				s=BeautifulSoup(f,"html.parser")
				for k in s.find_all("div",class_="_3liAhj"):
					products.append(k.find("a",class_="_2cLu-l").get("title"))
					if k.find("div",class_="hGSR34")!=None:
						ratings.append(float(k.find("div",class_="hGSR34").get_text()))
					else:
						ratings.append(float(0))
					if k.find("div",class_="_1vC4OE") !=None:
						price.append(k.find("div",class_="_1vC4OE").get_text())
					else:
						price.append(0)
					if k.find("div",class_="_1vC4OE") !=None:
						description.append(k.find("div",class_="_1rcHFq").get_text())
					else:
						description.append("SOORY! NO description")



			for i in range(len(products)):
				price[i]=int(re.sub("[^0-9&.]","",price[i]))
				user=Big(Product=products[i],Ratings=ratings[i],Price=price[i])
				db.session.add(user)
				db.session.commit()
				
				src[str(i)]={"PRODUCTS":products[i],"PRICES":price[i],"RATINGS":ratings[i]}

			session["TECH_PRODUCT"]=products
			session["TECH_PRICE"]=price
			session["TECH_RATINGS"]=ratings

			data=json.dumps(src,indent=5)
			#with open(".json","w") as file:
				#json.dump(data,file)


		return data
	return render_template("main_link.html")

@app.route("/config")
def config():
	return render_template("download.html")


@app.route("/download",methods=["GET","POST"])
def download():
	p=[]
	r=[]
	c=[]
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="root",
  	passwd="MYPASSWORD",
  	database="Scraped"
	)
	myc=mydb.cursor()
	myc.execute("SELECT *  FROM big")
	for i in myc:
		c.append(i[3])
		p.append(i[1])
		r.append(i[2])

	dataf=pd.DataFrame({"PRODUCTS":p,"RATINGS":r,"PRICES":c})
	oly=dataf.to_csv("massive.csv",sep=",")
	path="massive.csv"
	return send_file(path,as_attachment=True)








def create_csv():
	p=[]
	r=[]
	c=[]
	mydb = mysql.connector.connect(
  	host="localhost",
  	user="root",
  	passwd="MYPASSWORD",
  	database="Scraped"
	)
	myc=mydb.cursor()
	myc.execute("SELECT *  FROM big")
	for i in myc:
		c.append(i[3])
		p.append(i[1])
		r.append(i[2])

	dataf=pd.DataFrame({"PRODUCTS":p,"RATINGS":r,"PRICES":c})
	oly=dataf.to_csv("massive.csv",sep=",")




	






app.run()




			

			





		



