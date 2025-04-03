from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask, render_template, request, redirect, url_for, make_response
import user_management as dbHandler
from urllib.parse import urlparse, urljoin

# Code snippet for logging a message
# app.logger.critical("message")

app = Flask(__name__)

def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

def is_safe_url(target):
    ref_url = urlparse(request.host.url)
    test_url = urlparse(urljoin(request.host.url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
@@ -52,12 +59,11 @@ def home():
        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listFeedback()
            return render_template("/success.html", value=username, state=isLoggedIn)
            return render_template("success.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
            return render_template("index.html")
    else:
        return render_template("/index.html")

        return render_template("index.html")

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
