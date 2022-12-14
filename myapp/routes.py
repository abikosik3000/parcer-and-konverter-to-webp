#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myapp import app , db
from flask import Flask ,render_template , flash, request, redirect, url_for , send_from_directory
from flask_login import LoginManager, UserMixin  , login_required, login_user, current_user , logout_user
import myapp.controllers.loader_controller as loader_controller
import myapp.controllers.optimize_controller as optimize_controller
import myapp.controllers.login_controller as login_controller
from myapp.forms.login import LoginForm
from myapp.models.user import User

@app.route('/')
def get_main():
    return render_template('main.html' )

@login_required
@app.route('/cabinet' , methods=['GET'])
def get_cabinet():
    return current_user.email

@app.route('/optimize' , methods=['GET'])
def get_optimize():
    return optimize_controller.get_upload_from_site(app,request)
    
@app.route('/optimize' , methods=['POST'])
def post_optimize():
    return optimize_controller.post_upload_from_site(app,request)


'''
LOGIN PATH
'''
@app.route('/login', methods = ['GET', 'POST'])
def login():
    return login_controller.login()
    
@app.route('/register', methods = ['GET', 'POST'])
def register():
    return login_controller.register()
    
@app.route('/logout')
@login_required
def logout():
    return login_controller.logout()


'''
OTHER PATH
'''
@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

@app.route('/uploads/<path:name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

'''
@app.route('/upload' , methods=['GET'])
def get_upload():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def post_upload():
    return loader_controller.post_upload(app,request)
'''