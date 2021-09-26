from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect,url_for
import os
# from flask_bcrypt import Bcrypt
def loginCheck(param):
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return param
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin_index():
   
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
   return loginCheck(render_template('admin/index.html', posts=posts,portheads=portheads,headers=headers,aboutnames=aboutnames,services=services,serviceboxs=serviceboxs,feeds=feeds,tests=tests,icons=icons,blogs=blogs,contacts=contacts,logos=logos,panels=panels,heads=heads,menus=menus,ends=ends))
  
   


# 
# add
@app.route('/admin/head', methods=['GET','POST']) 
def head():
   heads=Menu.query.all()
   if request.method=='POST':
      head=Menu(
         menu_name=request.form['menu_name'],
      )     
      db.session.add(head)
      db.session.commit()
      return redirect('/admin/head')
   return loginCheck(render_template('admin/head.html',heads=heads))

@app.route("/admin/headdelete/<id>")
def headdelete(id):
   head=Menu.query.get(id)
   db.session.delete(head)
   db.session.commit()
   return loginCheck('/admin/head')


@app.route("/admin/headupdate/<id>" , methods=['GET','POST'])  
def headupdate(id):
   head=Menu.query.get(id)
   if request.method=='POST':
      head.menu_name=request.form['menu_name']
      db.session.commit()
      return redirect('/admin/head')
   return loginCheck (render_template('admin/headupdate.html',head=head))

# menu
@app.route('/admin/menu', methods=['GET','POST']) 
def menu():
   menus=SiteHeading.query.all()
   if request.method=='POST':
      menu=SiteHeading(
      menu_subheading=request.form['menu_subheading'],
      menu_heading=request.form['menu_heading'],
      menu_button_name=request.form['menu_button_name']
      )     
      db.session.add(menu)
      db.session.commit()
      return redirect('/admin/menu')
   return loginCheck(render_template('admin/menu.html',menus=menus))
   
   
@app.route("/admin/menudelete/<id>")
def menudelete(id):
   menu=SiteHeading.query.get(id)
   db.session.delete(menu)
   db.session.commit()
   return redirect('/admin/menu')

@app.route("/admin/menuupdate/<id>" , methods=['GET','POST'])  
def menuupdate(id):
    menu=SiteHeading.query.get(id)
    if request.method=='POST':
      menu.menu_subheading=request.form['menu_subheading']
      menu.menu_heading=request.form['menu_heading']
      menu.menu_button_name =request.form['menu_button_name']
      db.session.commit()
      return redirect('/admin/menuupdate')
    return loginCheck(render_template('admin/menu.html',menu=menu))

# about start
@app.route('/admin/aboutname', methods=['GET','POST']) 
def adminAbout():
   aboutnames=AboutHeading.query.all()
   if request.method=='POST':
      aboutname=AboutHeading(
         about_desc_name=request.form['about_desc_name'],
         about_heading_name=request.form['about_heading_name']
      )     
      db.session.add(aboutname)
      db.session.commit()
      return redirect('/admin/aboutname')
   return loginCheck(render_template('admin/aboutname.html',aboutnames=aboutnames))
   
@app.route("/admin/aboutdelete/<id>")
def aboutdelete(id):
   aboutname=AboutHeading.query.get(id)
   db.session.delete(aboutname)
   db.session.commit()
   return redirect('/admin/aboutname')


@app.route("/admin/aboutupdate/<id>" , methods=['GET','POST'])  
def aboutupdate(id):
   aboutname=AboutHeading.query.get(id)
   if request.method=='POST':
      aboutname.about_heading_name=request.form['about_heading_name']
      aboutname.about_desc_name=request.form['about_desc_name']
      db.session.commit()
      return redirect('/admin/aboutname')
   return loginCheck(render_template('admin/aboutupdate.html',aboutname=aboutname))

# panel
# add

@app.route('/admin/panel', methods=['GET','POST']) 
def panel():
   panels=AboutBox.query.all()
   if request.method=='POST':
      file=request.files['line_panel_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      panel=AboutBox(
         line_panel_subheading=request.form['line_panel_subheading'],
         line_panel_heading=request.form['line_panel_heading'],
         line_panel_title=request.form['line_panel_title'],
         line_panel_img=filename

      )     
      db.session.add(panel)
      db.session.commit()
      return redirect('/admin/panel')
   return loginCheck(render_template('admin/panel.html',panels=panels))

# delete
@app.route("/admin/paneldelete/<id>")
def paneldelete(id):
   panel=AboutBox.query.get(id)
   db.session.delete(panel)
   db.session.commit()
   return redirect('/admin/panel')


# update
@app.route("/admin/panelupdate/<id>" , methods=['GET','POST']) 
def panelupdate(id):
   panel=AboutBox.query.get(id)
   if request.method=='POST':
      file=request.files['line_panel_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      panel.line_panel_subheading=request.form['line_panel_subheading']
      panel.line_panel_heading=request.form['line_panel_heading']
      panel.line_panel_title=request.form['line_panel_title']
      panel.line_panel_img=filename
      db.session.commit()
      return redirect('/admin/panel')
   return loginCheck(render_template('admin/panelupdate.html',panel=panel))

# about end

# servies start 
# servicehead
# add
@app.route('/admin/serviceshead', methods=['GET','POST']) 
def ServicesHead():
   services=ServicesHeading.query.all()
   if request.method=='POST':
      services=ServicesHeading(
      services_subheading=request.form['services_subheading'],
      services_heading=request.form['services_heading']
      )     
      db.session.add(services)
      db.session.commit()
      return redirect('/admin/serviceshead')
   return loginCheck(render_template('admin/serviceshead.html',services=services))

# 

# delete
@app.route("/admin/servicesheaddelete/<id>")
def Servicesdelete(id):
   service=ServicesHeading.query.get(id)
   db.session.delete(service)
   db.session.commit()
   return redirect('/admin/serviceshead')
 
# 

# update
@app.route("/admin/servicesheadupdate/<id>" , methods=['GET','POST'])  
def Servicesupdate(id):
   service=ServicesHeading.query.get(id)
   if request.method=='POST':
      service.services_subheading=request.form['services_subheading']
      service.services_heading=request.form['services_heading']
      db.session.commit()
      return redirect('/admin/serviceshead')
   return loginCheck(render_template('admin/servicesheadupdate.html',service=service))

# 

# services box
# add
@app.route('/admin/servicesbox', methods=['GET','POST']) 
def servicesbox():
   serviceboxs=ServicesBox.query.all()
   if request.method=='POST':
      servicebox=ServicesBox(
         services_icon=request.form['services_icon'],
         services_title_heading=request.form['services_title_heading'],
         services_title=request.form['services_title']
      )     
      db.session.add(servicebox)
      db.session.commit()
      return redirect('/admin/servicesbox')
   return loginCheck(render_template('admin/servicesbox.html',serviceboxs=serviceboxs))

# 

# delete
@app.route("/admin/servicesboxdelete/<id>")
def Servicesboxdelete(id):
   servicebox=ServicesBox.query.get(id)
   db.session.delete(servicebox)
   db.session.commit()
   return redirect('/admin/servicesbox')
 
# 

# update
@app.route("/admin/servicesboxupdate/<id>" , methods=['GET','POST'])  
def Servicesboxupdate(id):
   servicebox=ServicesBox.query.get(id)
   if request.method=='POST':
         servicebox.services_icon=request.form['services_icon']
         servicebox.services_title_heading=request.form['services_title_heading']
         servicebox.services_title=request.form['services_title']
         db.session.commit()
         return redirect('/admin/servicesbox')
   return loginCheck(render_template('admin/servicesboxupdate.html',servicebox=servicebox))

# 

# services end

# portfolio start
@app.route('/admin/post', methods=['GET','POST']) 
def admin_post():
   posts=Post.query.all()
   if request.method=='POST':
      file=request.files['project_img']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      post=Post(
         project_name=request.form['project_name'],
         project_header=request.form['project_header'],
         project_img=filename
      )     
      db.session.add(post)
      db.session.commit()
      return redirect('/admin/post')
   return loginCheck(render_template('admin/post.html',posts=posts))


@app.route("/admin/postdelete/<id>")
def postdelete(id):
   post=Post.query.get(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/admin/post')

@app.route("/admin/postupdate/<id>" , methods=['GET','POST']) 
def postupdate(id):
   post=Post.query.get(id)
   if request.method=='POST':
      file=request.files['project_img']
      filename=file.filename
      file.save(os.path.join('app/static/uploads/',filename))
      post.project_name=request.form['project_name']
      post.project_header=request.form['project_header']
      post.project_img=filename
      db.session.commit()
      return redirect('/admin/post')
   return loginCheck(render_template('admin/postupdate.html',post=post))

# blog start 
# add
# Mehman Mirzeyev 1 a1/jpg
#Mehman Mirzeyv 2 a2.jpg
@app.route('/admin/blog', methods=['GET','POST']) 
def blog():
   blogs=Postjs.query.all()
   if request.method=='POST':
      file=request.files['project_img_js']
      filename=file.filename
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      blog=Postjs(
         project_name_js=request.form['project_name_js'],

         project_header_js =request.form['project_header_js'],
         project_desc_js=request.form['project_desc_js'],  
         project_client=request.form['project_client'],
         project_cat=request.form['project_cat'],
         close_icon=request.form['close_icon'],
         close_icon_name=request.form['close_icon_name'],
         project_img_js=filename
      )     
      db.session.add(blog)
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck(render_template('admin/blog.html',blogs=blogs))


# delete

@app.route("/admin/blogdelete/<id>")
def blogdelete(id):
   blog=Postjs.query.get(id)
   db.session.delete(blog)
   db.session.commit()
   return redirect('/admin/blog')

# update


@app.route("/admin/blogupdate/<id>" , methods=['GET','POST']) 
def blogupdate(id):
   blog=Postjs.query.get(id)
   if request.method=='POST':
      file=request.files['project_img_js']
      filename=file.filename
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      blog.project_name_js=request.form['project_name_js']
      blog.project_header_js =request.form['project_header_js']
      blog.project_desc_js=request.form['project_desc_js']  
      blog.project_client=request.form['project_client']
      blog.project_cat=request.form['project_cat']
      blog.close_icon=request.form['close_icon']
      blog.close_icon_name=request.form['close_icon_name']
      blog.project_img_js=filename
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck(render_template('admin/blogupdate.html',blog=blog))

# portfolio head

@app.route('/admin/porthead', methods=['GET','POST']) 
def admin_porthead():
   portheads=PostHeading.query.all()
   if request.method=='POST':
      porthead=PostHeading(
         portfolio_subheading=request.form['portfolio_subheading'],
         portfolio_heading=request.form['portfolio_heading']
      )     
      db.session.add(porthead)
      db.session.commit()
      return redirect('/admin/porthead')
   return loginCheck(render_template('admin/porthead.html',portheads=portheads))
   
@app.route("/admin/portupdate/<id>" , methods=['GET','POST'])  
def portupdate(id):
   porthead=PostHeading.query.get(id)
   if request.method=='POST':
      porthead.portfolio_subheading=request.form['portfolio_subheading']
      porthead.portfolio_heading=request.form['portfolio_heading']
      db.session.commit()
      return redirect('/admin/porthead')
   return loginCheck(render_template('admin/portheadupdate.html',porthead=porthead))

@app.route("/admin/portdelete/<id>")
def portdelete(id):
   porthead=PostHeading.query.get(id)
   db.session.delete(porthead)
   db.session.commit()
   return redirect('/admin/porthead')

#

# portfolio end


# testimionals start
# add
@app.route('/admin/feedbackheading', methods=['GET','POST']) 
def feedbackheading():
   feeds=FeedbackHeading.query.all()
   if request.method=='POST':
      feed=FeedbackHeading(
         testi_subheading=request.form['testi_subheading'],
         testi_heading=request.form['testi_heading']
      
      )     
      db.session.add(feed)
      db.session.commit()
      return redirect('/admin/feedbackheading')
   return loginCheck (render_template('admin/feedbackheading.html',feeds=feeds))

# 


# delete
@app.route("/admin/feedbackheadingdelete/<id>")
def fedbackheadindelete(id):
   feed=FeedbackHeading.query.get(id)
   db.session.delete(feed)
   db.session.commit()
   return redirect('/admin/feedbackheading')
 
# 

@app.route("/admin/feedbackheadingupdate/<id>" , methods=['GET','POST'])  
def feedbackheadingupdate(id):
   feed=FeedbackHeading.query.get(id)
   if request.method=='POST':
         feed.testi_subheading=request.form['testi_subheading']
         feed.testi_heading=request.form['testi_heading']
         db.session.commit()
         return redirect('/admin/feedbackheading')
   return loginCheck(render_template('admin/feedbackheadingupdate.html',feed=feed))
# 

# Feedback start
# add
@app.route('/admin/feedback', methods=['GET','POST']) 
def feedback():
   tests=Feedback.query.all()
   if request.method=='POST':
      file_commenter=request.files['commenter_img']
      filename_commenter_name=file_commenter.filename
      file_commenter.save(os.path.join (app.config['UPLOAD_FOLDER'],filename_commenter_name))
      test=Feedback(
         commenter_name=request.form['commenter_name'],
         commenter_title=request.form['commenter_title'],
         commenter_twitter=request.form['commenter_twitter'],
         commenter_facebook =request.form['commenter_facebook'],
         commenter_linkedin=request.form['commenter_linkedin'],
         commenter_img=filename_commenter_name

      )     
      db.session.add(test)
      db.session.commit()
      return redirect('/admin/feedback')
   return loginCheck(render_template('admin/feedback.html',tests=tests))

#delete 

@app.route("/admin/feedbackdelete/<id>")
def feedbackdelete(id):
   test=Feedback.query.get(id)
   db.session.delete(test)
   db.session.commit()
   return redirect('/admin/feedback')

# 

# update

@app.route("/admin/feedbackupdate/<id>" , methods=['GET','POST']) 
def feedbackupdate(id):
   test=Feedback.query.get(id)
   if request.method=='POST':
      file_commenter=request.files['commenter_img']
      filename_commenter_name=file_commenter.filename
      file_commenter.save(os.path.join (app.config['UPLOAD_FOLDER'],filename_commenter_name))
      test.commenter_name=request.form['commenter_name']
      test.commenter_title=request.form['commenter_title']
      test.commenter_twitter=request.form['commenter_twitter']
      test.commenter_facebook =request.form['commenter_facebook']
      test.commenter_linkedin=request.form['commenter_linkedin']
      test.commenter_img=filename_commenter_name
      db.session.commit()
      return redirect('/admin/feedback')
   return loginCheck(render_template('admin/feedbackupdate.html',test=test))

# 

@app.route('/admin/fkend', methods=['GET','POST']) 
def end():
   ends=Aboutboxend.query.all()
   if request.method=='POST':
      end=Aboutboxend(
      line_panel_desc=request.form['line_panel_desc'],
   
      )     
      db.session.add(end)
      db.session.commit()
      return redirect('/admin/fkend')
   return loginCheck (render_template('admin/fkend.html',ends=ends))
   
   
@app.route("/admin/fkenddelete/<id>")
def fkenddelete(id):
   end=Aboutboxend.query.get(id)
   db.session.delete(end)
   db.session.commit()
   return redirect('/admin/fkend')

@app.route("/admin/fkendupdate/<id>" , methods=['GET','POST'])  
def fkendupdate(id):
   end=Aboutboxend.query.get(id)
   if request.method=='POST':
      end.line_panel_desc=request.form['line_panel_desc']
      db.session.commit()
      return redirect('/admin/fkendupdate')
   return loginCheck(render_template('admin/fkend.html',end=end))

  
# Feedback end

# testimionals end

# logo 
# add
@app.route('/admin/logo', methods=['GET','POST']) 
def logoadd():
   logos=Logo.query.all()
   if request.method=='POST':
      file=request.files['logo_img']
      file_logo_img=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],file_logo_img))
      logo=Logo(
         logo_name=request.form['logo_name'],
         logo_img=file_logo_img
      )     
      db.session.add(logo)
      db.session.commit()
      return redirect('/admin/logo')
   return loginCheck (render_template('admin/logo.html',logos=logos))


# delete
@app.route("/admin/logodelete/<id>")
def logodelete(id):
   logo=Logo.query.get(id)
   db.session.delete(logo)
   db.session.commit()
   return redirect('/admin/logo')

# 

# update

@app.route("/admin/logoupdate/<id>" , methods=['GET','POST']) 
def logoupdate(id):
   logo=Logo.query.get(id)
   if request.method=='POST':
      file_logo_img=request.files['logo_img']
      file_logo_name=file_logo_img.filename
      file_logo_img.save(os.path.join (app.config['UPLOAD_FOLDER'],file_logo_name))
      logo.logo_name=request.form['logo_name']
      logo.logo_img=request.form['logo_img']
      db.session.commit()
      return redirect('/admin/logo')
   return loginCheck (render_template('admin/logoupdate.html',logo=logo))

# 

# contact start

# contact heading 
# add

@app.route('/admin/contactheading', methods=['GET','POST']) 
def contactheading():
   contacts=ContactHeading.query.all()
   if request.method=='POST':
      contact=ContactHeading(
      contact_subheading_name =request.form['contact_subheading_name'],
      contact_heading_name=request.form['contact_heading_name']
      )     
      db.session.add(contact)
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck(render_template('admin/contactheading.html',contacts=contacts))
   
   # update
@app.route("/admin/contactheadingupdate/<id>" , methods=['GET','POST'])  
def contactupdate(id):
   contact=ContactHeading.query.get(id)
   if request.method=='POST':
      contact.contact_subheading_name=request.form['contact_subheading_name']
      contact.contact_heading_name=request.form['contact_heading_name']
      db.session.commit()
      return redirect('/admin/contact')
   return loginCheck(render_template('admin/contactheading.html',contact=contact))

@app.route("/admin/contactheadingdelete/<id>")
def contactdelete(id):
   contact=ContactHeading.query.get(id)
   db.session.delete(contact)
   db.session.commit()
   return redirect('/admin/contactheading')


# contact end


# social-icon start
@app.route('/admin/social', methods=['GET','POST']) 
def socicalIcon():
   icons= SocicalIcon.query.all()
   if request.method=='POST':
      icon=SocicalIcon(
      social_icon_name=request.form['social_icon_name'],
      social_icon=request.form['social_icon'],
      social_icon_link=request.form['social_icon_link']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/social')
   return loginCheck(render_template('admin/social.html',icons=icons))


# delete
@app.route("/admin/socialdelete/<id>")
def socialdelete(id):
   icon = SocicalIcon.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/social')
 
# 

# update
@app.route("/admin/socialupdate/<id>" , methods=['GET','POST'])  
def socialupdate(id):
   icon = SocicalIcon.query.get(id)
   if request.method=='POST':
         icon.social_icon_name=request.form['social_icon_name']
         icon.social_icon=request.form['social_icon']
         icon.social_icon_link=request.form['social_icon_link']
         db.session.commit()
         return redirect('/admin/social')
   return loginCheck (render_template('admin/socialupdate.html',icon=icon))

# 


@app.route("/admin/contactformdelete/<id>")
def contactformdelete(id):
   contactform = ContactMe.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect('/admin/contactform')



# social-icon end








