from flask import Flask,request,redirect,render_template,flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)	



db_name = 'blogposts.db'
app.config['SECRET_KEY'] = 'djncdjskdh834u4b3o3300civjfj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
data_base = SQLAlchemy(app)

class BlogPosts(data_base.Model):
	id = data_base.Column(data_base.Integer,primary_key=True)
	title = data_base.Column(data_base.String,nullable=False) 
	author = data_base.Column(data_base.String,nullable=True,default="Unknown")
	content = data_base.Column(data_base.String,nullable=False)
	post_date = data_base.Column(data_base.DateTime,nullable=False)
	
	def __repr__(self):
		return 'Blog Post ' + str(self.id)



@app.route('/allposts',methods=['GET','POST'])
def index():
	if request.method=='POST':
		title = request.form['title']
		content = request.form['content']
		author = request.form['author']
		new_post = BlogPosts(title=title,author=author,content=content,post_date=datetime.now())
		data_base.session.add(new_post)
		data_base.session.commit()
		return redirect('/allposts')
	else:
	   all_posts = BlogPosts.query.all()
	   return render_template('posts.html',posts=all_posts) 

@app.route("/posts/delete/<int:id>") 
def delete(id):
    post = BlogPosts.query.get_or_404(id)
    data_base.session.delete(post)
    data_base.session.commit()
    return redirect("/allposts")
	                                     
@app.route("/posts/edit/<int:id>",methods=["GET","POST"]) 
def editId(id): 
    post = BlogPosts.query.get_or_404(id)
    if request.method=="POST": 
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        data_base.session.commit() 
        flash("edited successfully")
        return redirect("/allposts")
    else:
    	return render_template("edit.html", post=post)
    	
@app.route("/posts/newpost")
def newpost(): 
    return render_template("newPost.html")
                                                                                                 	                                         																																														                                                                                                	                                                                                                
                                                                                                 	                                         																																														                                                                                                	                                                                                                
	                                                                                                	                                         																																														                                                                                                	                                                                                                
	                                                                                                	                                         																																													
if __name__=='__main__':
	app.run(debug=True)