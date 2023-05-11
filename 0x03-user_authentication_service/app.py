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
