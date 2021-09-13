# from flask import Blueprint, request, redirect, url_for, render_template

# auth = Blueprint('auth', __name__)

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     # POST REQUEST:
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Username/password incorrect. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     # GET REQUEST:
#     else:
#         return '<h1>Login</h1>'


# @auth.route('/logout')
# def logout():
#     return '<p>logout</p>'


# @auth.route('/sign-up')
# def sign_up():
#     return '<p>sign up</p>'
