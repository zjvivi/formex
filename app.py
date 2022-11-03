from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_bootstrap import Bootstrap
import forms

app = Flask(__name__)
bootstrap=Bootstrap(app)

app.config['SECRET_KEY']='hello zjvivi'

@app.route('/profile')
def profile():
    name=request.args.get('name')

    if not name:
        from flask import redirect
        return redirect("/login")
    else:
        return name


@app.route('/login')
def login():
   return 'login page'

@app.route('/user/<int:user_id>')
def user_detail(user_id):
   return '用户编号为%s的个人详情页' % user_id

@app.get('/search')
def search():
   url=url_for("user_detail",user_id=1,user_name='zjvivi')
   return redirect(url)

@app.route('/',methods=['GET','POST'])
def index():

    form = forms.NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name!= form.name.data:
            flash("已提交用户名")
        session["name"] =form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get("name"))


if __name__ == '__main__':
    app.run()
