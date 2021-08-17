from flask import Flask, render_template, request, redirect,session
from flask_app import app
from flask_app.controllers import dojos
app.secret_key = 'Felix RULZ'



if __name__ == "__main__":
    app.run(debug=True)