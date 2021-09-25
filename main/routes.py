from admin.routes import loginCheck
from app import app
from app.models import *
from flask import render_template,request,redirect



@app.route('/')
def index():
    posts=Post.query.all()
    portheads=PostHeading.query.all()
    headers=PostHeading01.query.all()
    aboutnames=AboutHeading.query.all()
    services=ServicesHeading.query.all()
    serviceboxs=ServicesBox.query.all()
    feeds=FeedbackHeading.query.all()
    tests=Feedback.query.all()
    icons=SocicalIcon.query.all()
    blogs=Postjs.query.all()
    contacts=ContactHeading.query.all()
    logos=Logo.query.all()
    panels=AboutBox.query.all()
    heads=Menu.query.all()
    menus=SiteHeading.query.all()
    ends=Aboutboxend.query.all()
    return render_template('main/index.html',posts=posts,portheads=portheads,headers=headers, aboutnames=aboutnames,services=services,serviceboxs=serviceboxs,feeds=feeds,tests=tests,icons=icons,blogs=blogs,contacts=contacts,logos=logos,panels=panels,heads=heads,menus=menus,ends=ends)


@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   contactforms =ContactMe.query.all()
   if request.method=='POST':
      contactform=ContactMe(
   user_name=request.form['user_name'],
   user_email=request.form['user_email'],
   user_phone=request.form['user_phone'],
   user_message=request.form['user_message']

      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/admin/contactform')
   return loginCheck (render_template('admin/contactform.html',contactforms=contactforms ))
   