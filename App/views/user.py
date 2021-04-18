from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.models import User

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_views.route('/login')
def index():
  return render_template('login.html')

@user_views.route('/login', methods=['POST'])
def loginAction():
    form = LogIn()
    if form.validate_on_submit(): 
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): 
        flash('Logged in successfully.') 
        login_user(user) 
        return redirect(url_for('todos')) 
    flash('Invalid credentials')
    return redirect(url_for('index'))




@user_views.route('/api/users')
def client_app():
    users = User.query.all()
    if not users:
        return jsonify([])
    users = [user.toDict() for user in users]
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')