from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from may_blog.models import Post, db
from may_blog.forms import BlogPostForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/createposts', methods=['GET','POST'])
@login_required
def createposts():
    print(current_user.id)
    form = BlogPostForm()
    print (form.content.data)
    
    if request.method == 'POST' and form.validate():
        print('here')
        title = form.title.data
        content = form.content.data
        user_id = (current_user.id)
        print('\n', title, content)

        post = Post(title, content, user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('site.createposts'))
    print('there')
    
    return render_template('createposts.html', form = form)