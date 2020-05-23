import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/login',methods=["GET", "POST"])
def login():

    _userId = request.args.get('userId')
    _password = request.args.get('pwd')
    
    if request.method=="GET" or request.method=="POST":
        
        if  _userId == "user" and _password == "user":
            
            respDict = {
                    
                    'username':_userId,
                    'name':'Bobby',
                    'status':'0'
                    
            }
            
            resp = jsonify(respDict)
            return resp
        
        else:
            
            resp = jsonify('Invalid Username/Password')
            return resp
    
    
@app.route('/register',methods=["GET", "POST"])
def register():

    _userId = request.args.get('userId')
    _fName = request.args.get('fn')
    _lName = request.args.get('ln')
    _gender = request.args.get('gender')
    _mobile = request.args.get('mobile')
    _email = request.args.get('email')
    
    if request.method=="GET" or request.method=="POST":
        
        if  _userId == "user" and _mobile == "0803":
            
            name = _fName +' '+ _lName
            respDict = {
                    
                    'username':_userId,
                    'name':name,
                    'gender':_gender,
                    'mobile':_mobile,
                    'email':_email,
                    'status':'0'
                    
            }
              
            resp = jsonify(respDict)
            return resp
        
        else:
            
            resp = jsonify('Invalid Username/Password')
            return resp
    

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run()