#!/usr/bin/env python3
""" Flask Application """

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


@app.route("/", methods=["GET"], strict_slashes=False)
def root():
    """Root endpoint"""
    return jsonify({"message": "Bienvenue"})
