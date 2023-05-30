from flask import Flask,send_file,request,redirect
import sqlite3



app = Flask(__name__,static_folder="static",static_url_path="/static")


@app.get("/")
def index():
    return send_file("static/index.html")

@app.post("/signup")
def register():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    password = request.form.get("createpassword")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(f"insert into users(name,email,phone,password) values('{name}','{email}','{phone}','{password}')")
    con.commit()
    con.close()
    print(name,phone,email,password)
    return redirect("static/login.html")


@app.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res =  cur.execute(f"select * from users where name='{username}'").fetchone()
    responce = ""
    if(res==None):
        responce = "<h2>user not found</h2>"
    elif(res[-1]!=password):
        responce = "<h2>invalid credentials</h2>"
    else:
       responce = redirect("static/index.html")
    con.commit()
    con.close()
    return responce
    




app.run(debug=True,port=80)