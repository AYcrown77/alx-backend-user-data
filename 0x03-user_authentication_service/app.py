#!/usr/bin/env python3
""" Flask Application module"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def root():
    """Root endpoint"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Register Users"""
    email = request.form["email"]
    password = request.form["password"]
    try:
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
            })
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
